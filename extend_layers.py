# <-*- encoding:utf-8 -*->
"""
    self-defined external Layer
"""

try:
    import cPickle as pickle
except ImportError:
    import pickle
import numpy as np
import theano
import theano.tensor as T
import lasagne
import config
__author__ = 'jacoxu & shin'


class InnerProductLayer(lasagne.layers.MergeLayer):

    def __init__(self, incomings, nonlinearity=None, **kwargs):
        super(InnerProductLayer, self).__init__(incomings, **kwargs)
        self.nonlinearity = nonlinearity
        if len(incomings) != 2:
            raise NotImplementedError

    def get_output_shape_for(self, input_shapes):
        return input_shapes[0][:2]

    def get_output_for(self, inputs, **kwargs):
        M = inputs[0]
        u = inputs[1]
        output = T.batched_dot(M, u)
        if self.nonlinearity is not None:
            output = self.nonlinearity(output)
        return output


class BatchedDotLayer(lasagne.layers.MergeLayer):

    def __init__(self, incomings, **kwargs):
        super(BatchedDotLayer, self).__init__(incomings, **kwargs)
        if len(incomings) != 2:
            raise NotImplementedError

    def get_output_shape_for(self, input_shapes):
        return input_shapes[1][0], input_shapes[1][2]

    def get_output_for(self, inputs, **kwargs):
        return T.batched_dot(inputs[0], inputs[1])


class SumLayer(lasagne.layers.Layer):

    def __init__(self, incoming, axis, **kwargs):
        super(SumLayer, self).__init__(incoming, **kwargs)
        self.axis = axis

    def get_output_shape_for(self, input_shape):
        return input_shape[:self.axis] + input_shape[self.axis+1:]

    def get_output_for(self, input, **kwargs):
        return T.sum(input, axis=self.axis)


class TemporalEncodingLayer(lasagne.layers.Layer):
    def __init__(self, incoming, time_W=lasagne.init.Normal(std=0.1), **kwargs):
        super(TemporalEncodingLayer, self).__init__(incoming, **kwargs)
        self.time_W = self.add_param(time_W, self.input_shape[-2:], name="T")

    def get_output_shape_for(self, input_shape):
        return input_shape

    def get_output_for(self, sent_vecs, **kwargs):
        return sent_vecs + self.time_W


class TemporalEncodingLayerMask(lasagne.layers.MergeLayer):
    def __init__(self, incomings, time_W=lasagne.init.Normal(std=0.1), **kwargs):
        super(TemporalEncodingLayerMask, self).__init__(incomings, **kwargs)
        if len(incomings) != 2:
            raise NotImplementedError
        self.time_W = self.add_param(time_W, self.input_shapes[0][-2:], name="T")

    def get_output_shape_for(self, input_shapes):
        return input_shapes[0]

    def get_output_for(self, inputs, **kwargs):
        seq_vecs = inputs[0]
        seq_embed_mask = inputs[1]
        return T.mul(seq_vecs + self.time_W, seq_embed_mask)


class ContentAttentionLayer(lasagne.layers.MergeLayer):
    """Attention mechanism: att = v'(Wq+Um), softmax"""
    def __init__(self, incomings, W_align, U_align, v_align,
                 batch_size, max_seq_story, max_sent_enc, embedding_size, align_hidden_size, top_k,
                 nonlinearity=lasagne.nonlinearities.softmax, **kwargs):
        super(ContentAttentionLayer, self).__init__(incomings, **kwargs)
        if len(incomings) != len(('l_C_embedding_flatten', 'l_queries_vec', 'l_stories_in', 'l_seq_prob_mem_nn')):
            raise NotImplementedError
        self.batch_size = batch_size
        self.max_seq_story = max_seq_story
        self.max_sent_enc = max_sent_enc
        self.top_k = top_k
        self.nonlinearity = nonlinearity
        self.W_align = self.add_param(W_align, (embedding_size, align_hidden_size), name="word_mem_W_align")
        self.U_align = self.add_param(U_align, (embedding_size, align_hidden_size), name="word_mem_U_align")
        self.v_align = self.add_param(v_align, (align_hidden_size, 1), name="word_mem_v_align")

    def get_output_shape_for(self, input_shapes):
        return input_shapes[0]

    def get_output_for(self, inputs, **kwargs):
        l_C_embedding_flatten = inputs[0]  # (batch_size, max_seq_story * max_sent_enc, embedding_size)
        l_queries_vec = inputs[1]  # (batch_size, embedding_size)
        l_stories_in = inputs[2]  # (self.batch_size * self.max_seq_story * self.max_sent_enc, )
        l_seq_prob_mem_nn = inputs[3]  # (self.batch_size, self.max_seq_story)
        l_words_mask = T.neq(l_stories_in, 0)
        ############
        if (self.top_k < 0) or (self.top_k > self.max_seq_story):
            l_words_mask = l_words_mask
        else:
            non_k_max_size = self.max_seq_story - self.top_k
            batch_size_idx = [i for i in range(self.batch_size)] * non_k_max_size
            batch_size_idx = np.array(batch_size_idx).reshape(non_k_max_size, self.batch_size).T
            batch_size_idx = batch_size_idx.reshape((non_k_max_size*self.batch_size,))
            seq_prob_non_k_max_idx = T.argsort(l_seq_prob_mem_nn, axis=1)[:, :non_k_max_size]
            seq_prob_non_k_max_idx = seq_prob_non_k_max_idx.reshape((non_k_max_size*self.batch_size,))
            l_words_mask = T.set_subtensor(l_words_mask[batch_size_idx, seq_prob_non_k_max_idx, :], 0)
        ############
        l_words_mask = l_words_mask.reshape((self.batch_size, self.max_seq_story*self.max_sent_enc))
        # (batch_size, max_seq_story * max_sent_enc, embedding_size) dot (embedding_size, align_hidden_size)
        # -> (batch_size, max_seq_story * max_sent_enc, align_hidden_size)
        hUa = T.dot(l_C_embedding_flatten, self.U_align)
        # (batch_size, embedding_size) * (embedding_size, align_hidden_size)
        # -> (batch_size, align_hidden_size)
        sWa = T.dot(l_queries_vec, self.W_align)
        # -> (batch_size, 1, align_hidden_size)
        sWa = sWa.dimshuffle(0, 'x', 1)
        # -> (batch_size, max_seq_story * max_sent_enc, align_hidden_size)
        tanh_sWahUa = lasagne.nonlinearities.tanh(sWa+hUa)
        #  -> (batch_size, max_seq_story * max_sent_enc, 1)
        enerage = T.dot(tanh_sWahUa, self.v_align)
        #  -> (batch_size, max_seq_story * max_sent_enc)
        enerage = T.reshape(enerage, (enerage.shape[0], enerage.shape[1]))
        enerage = T.mul(enerage, l_words_mask) - (1-l_words_mask)*1000000
        alpha = self.nonlinearity(enerage)
        return alpha


class MaskingLayer(lasagne.layers.Layer):
    def __init__(self, incoming, **kwargs):
        super(MaskingLayer, self).__init__(incoming, **kwargs)

    def get_output_shape_for(self, input_shape):
        return input_shape

    def get_output_for(self, input, **kwargs):
        return T.neq(input, 0)


class TransposedDenseLayer(lasagne.layers.DenseLayer):

    def __init__(self, incoming, num_units, W=lasagne.init.GlorotUniform(),
                 b=lasagne.init.Constant(0.), nonlinearity=lasagne.nonlinearities.rectify,
                 **kwargs):
        super(TransposedDenseLayer, self).__init__(incoming, num_units, W, b, nonlinearity, **kwargs)

    def get_output_shape_for(self, input_shape):
        return input_shape[0], self.num_units

    def get_output_for(self, input, **kwargs):
        if input.ndim > 2:
            input = input.flatten(2)

        activation = T.dot(input, self.W.T)
        if self.b is not None:
            activation = activation + self.b.dimshuffle('x', 0)
        return self.nonlinearity(activation)


class Repeat(lasagne.layers.Layer):
    def __init__(self, incoming, n, **kwargs):
        super(Repeat, self).__init__(incoming, **kwargs)
        self.n = n

    def get_output_shape_for(self, input_shape):
        return input_shape[0], self.n, input_shape[1]

    def get_output_for(self, input, **kwargs):
        assert input.ndim == 2
        input = input.dimshuffle((0, 'x', 1))
        return T.extra_ops.repeat(input, self.n, axis=1)


class WordLevelMemoryLayer(lasagne.layers.MergeLayer):
    def __init__(self, incomings, vocab, A_embed_W, A_time_W, C_embed_W, W_align, U_align, v_align,
                 non_linearity=lasagne.nonlinearities.softmax, **kwargs):
        super(WordLevelMemoryLayer, self).__init__(incomings, **kwargs)
        if len(incomings) != len(('l_queries_vec', 'l_stories_in', 'l_stories_pe_in', 'l_seq_embed_masks_in')):
            raise NotImplementedError

        # output size: [batch_size, embed_size]
        batch_size, embedding_size = self.input_shapes[0]
        batch_size, max_seq_story, max_sent_enc = self.input_shapes[1]

        l_queries_vec = lasagne.layers.InputLayer(shape=(batch_size, embedding_size))
        l_stories_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc))
        l_stories_pe_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc, embedding_size))
        l_seq_embed_masks_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story))
        # # reshape
        l_stories_emb = lasagne.layers.ReshapeLayer(l_stories_in, shape=(batch_size * max_seq_story * max_sent_enc, ))
        l_A_embedding = lasagne.layers.EmbeddingLayer(l_stories_emb, len(vocab) + 1, embedding_size, W=A_embed_W,
                                                      name='A_embedding_word_mem')
        # reshape back
        l_A_embedding = lasagne.layers.ReshapeLayer(l_A_embedding, shape=(batch_size, max_seq_story, max_sent_enc,
                                                                          embedding_size))
        l_A_embedding = lasagne.layers.ElemwiseMergeLayer((l_A_embedding, l_stories_pe_in), merge_function=T.mul)
        # sum all the words in one sentence
        l_A_stories_vec = SumLayer(l_A_embedding, axis=2)

        if config.enable_time:
            l_A_stories_vec = TemporalEncodingLayerMask((l_A_stories_vec, l_seq_embed_masks_in), time_W=A_time_W,
                                                        name='A_time_word_mem')

        # InnerProduct((batch32, seq10, embed20) * (batch32 * embed20)) --> (batch32, seq10)
        l_seq_prob_mem_nn = InnerProductLayer((l_A_stories_vec, l_queries_vec), nonlinearity=non_linearity)
        l_C_embedding = lasagne.layers.EmbeddingLayer(l_stories_emb, len(vocab) + 1, embedding_size, W=C_embed_W,
                                                      name='C_embedding_word_mem')
        self.C_embed_W = l_C_embedding.W
        l_C_embedding_flatten = lasagne.layers.ReshapeLayer(l_C_embedding,
                                                            shape=(batch_size, max_seq_story * max_sent_enc,
                                                                   embedding_size))

        l_stories_gru = lasagne.layers.ReshapeLayer(l_stories_in, shape=(batch_size, max_seq_story * max_sent_enc))
        l_words_mask = MaskingLayer(l_stories_gru)

        l_gru_forward = lasagne.layers.recurrent.GRULayer(l_C_embedding_flatten, num_units=embedding_size,
                                                          backwards=False, mask_input=l_words_mask)
        l_gru_backward = lasagne.layers.recurrent.GRULayer(l_C_embedding_flatten, num_units=embedding_size,
                                                           backwards=True, mask_input=l_words_mask)
        l_C_embedding_flatten = lasagne.layers.ElemwiseSumLayer((l_gru_forward, l_gru_backward))
        l_word_prob_word_mem = ContentAttentionLayer((l_C_embedding_flatten, l_queries_vec, l_stories_in,
                                                     l_seq_prob_mem_nn),
                                                     W_align=W_align, U_align=U_align, v_align=v_align,
                                                     batch_size=batch_size, max_seq_story=max_seq_story,
                                                     max_sent_enc=max_sent_enc, embedding_size=embedding_size,
                                                     align_hidden_size=embedding_size, top_k=config.top_k,
                                                     nonlinearity=lasagne.nonlinearities.softmax)

        self.l_queries_vec = l_queries_vec
        self.l_stories_in = l_stories_in
        self.l_stories_pe_in = l_stories_pe_in
        self.l_seq_embed_masks_in = l_seq_embed_masks_in

        self.model = l_word_prob_word_mem

        params = lasagne.layers.helper.get_all_params(self.model, trainable=True)
        values = lasagne.layers.helper.get_all_param_values(self.model, trainable=True)
        for p, v in zip(params, values):
            self.add_param(p, v.shape, name=p.name)

    def get_output_shape_for(self, input_shapes):
        return lasagne.layers.helper.get_output_shape(self.model)

    def get_output_for(self, inputs, **kwargs):
        return lasagne.layers.helper.get_output(self.model, {self.l_queries_vec: inputs[0],
                                                             self.l_stories_in: inputs[1],
                                                             self.l_stories_pe_in: inputs[2],
                                                             self.l_seq_embed_masks_in: inputs[3]})


class SentLevelMemoryLayer(lasagne.layers.MergeLayer):

    def __init__(self, incomings, vocab, embedding_size, A_embed_W, A_time_W, C_embed_W, C_time_W,
                 non_linearity=lasagne.nonlinearities.softmax, hops_num=0, **kwargs):
        super(SentLevelMemoryLayer, self).__init__(incomings, **kwargs)
        if len(incomings) != len(('l_stories_in', 'l_queries_vec', 'l_stories_pe_in', 'l_seq_embed_masks_in')):
            raise NotImplementedError

        batch_size, max_seq_story, max_sent_enc = self.input_shapes[0]

        l_stories_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc))
        l_queries_vec = lasagne.layers.InputLayer(shape=(batch_size, embedding_size))
        l_stories_pe_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc, embedding_size))
        l_seq_embed_masks_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story))
        # reshape
        l_stories_in = lasagne.layers.ReshapeLayer(l_stories_in, shape=(batch_size * max_seq_story * max_sent_enc, ))
        l_A_embedding = lasagne.layers.EmbeddingLayer(l_stories_in, len(vocab) + 1, embedding_size, W=A_embed_W,
                                                      name='A_embedding'+str(hops_num))
        self.A_embed_W = l_A_embedding.W
        # reshape back
        l_A_embedding = lasagne.layers.ReshapeLayer(l_A_embedding, shape=(batch_size, max_seq_story, max_sent_enc,
                                                                          embedding_size))
        l_A_embedding = lasagne.layers.ElemwiseMergeLayer((l_A_embedding, l_stories_pe_in), merge_function=T.mul)
        # sum all the words in one sentence
        l_A_stories_vec = SumLayer(l_A_embedding, axis=2)
        if config.enable_time:
            l_A_stories_vec = TemporalEncodingLayerMask((l_A_stories_vec, l_seq_embed_masks_in), time_W=A_time_W,
                                                        name='A_time'+str(hops_num))
            self.A_time_W = l_A_stories_vec.time_W

        l_C_embedding = lasagne.layers.EmbeddingLayer(l_stories_in, len(vocab) + 1, embedding_size, W=C_embed_W,
                                                      name='C_embedding'+str(hops_num))
        self.C_embed_W = l_C_embedding.W
        l_C_embedding = lasagne.layers.ReshapeLayer(l_C_embedding, shape=(batch_size, max_seq_story, max_sent_enc,
                                                                          embedding_size))
        l_C_embedding = lasagne.layers.ElemwiseMergeLayer((l_C_embedding, l_stories_pe_in), merge_function=T.mul)
        l_C_stories_vec = SumLayer(l_C_embedding, axis=2)
        if config.enable_time:
            l_C_stories_vec = TemporalEncodingLayerMask((l_C_stories_vec, l_seq_embed_masks_in), time_W=C_time_W,
                                                        name='C_time'+str(hops_num))
            self.C_time_W = l_C_stories_vec.time_W
        # batch_dot(batch,32 * seq,10 * embed,20, batch,32 * embed,20) -> batch,32 * seq,10
        l_prob = InnerProductLayer((l_A_stories_vec, l_queries_vec), nonlinearity=non_linearity)
        l_weighted_output = BatchedDotLayer((l_prob, l_C_stories_vec))

        l_sum = lasagne.layers.ElemwiseSumLayer((l_weighted_output, l_queries_vec))

        self.l_stories_in = l_stories_in
        self.l_queries_vec = l_queries_vec
        self.l_stories_pe_in = l_stories_pe_in
        self.l_seq_embed_masks_in = l_seq_embed_masks_in

        self.model = l_sum

        params = lasagne.layers.helper.get_all_params(self.model, trainable=True)
        values = lasagne.layers.helper.get_all_param_values(self.model, trainable=True)
        for p, v in zip(params, values):
            self.add_param(p, v.shape, name=p.name)

        zero_vec_tensor = T.vector()
        self.zero_vec = np.zeros(embedding_size, dtype=theano.config.floatX)
        self.set_zero = theano.function([zero_vec_tensor], updates=[(x, T.set_subtensor(x[0, :], zero_vec_tensor))
                                                                    for x in [self.A_embed_W, self.C_embed_W]])

    def get_output_shape_for(self, input_shapes):
        return lasagne.layers.helper.get_output_shape(self.model)

    def get_output_for(self, inputs, **kwargs):
        return lasagne.layers.helper.get_output(self.model, {self.l_stories_in: inputs[0],
                                                             self.l_queries_vec: inputs[1],
                                                             self.l_stories_pe_in: inputs[2],
                                                             self.l_seq_embed_masks_in: inputs[3]})

    def reset_zero(self):
        self.set_zero(self.zero_vec)
