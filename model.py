# -*- coding: utf8 -*-
from __future__ import division
import lasagne
import numpy as np
import theano
import theano.tensor as T
import time
from sklearn import metrics
from sklearn.preprocessing import label_binarize
from extend_layers import SumLayer, TransposedDenseLayer, SentLevelMemoryLayer, WordLevelMemoryLayer
import config

from model_init import ModelInit
__author__ = 'jacoxu & shin'


class Model(ModelInit):
    def __init__(self, _log_file):
        super(Model, self).__init__(_log_file)
        self.log_file = _log_file
        self.networks = self.build_network()

    def build_network(self):
        batch_size = config.batch_size
        embed_size = config.embed_size
        max_seq_story, max_sent_enc, vocab = self.max_seq_story, self.max_sent_enc, self.vocab
        stories, queries, answers = self.stories, self.queries, self.answers

        story_texts, query_texts = self.story_texts, self.query_texts

        # position encoding (pe)
        stories_pe, queries_pe = self.stories_pe, self.queries_pe
        seq_embed_masks = self.seq_masks

        l_stories_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc))
        l_queries_in = lasagne.layers.InputLayer(shape=(batch_size, max_sent_enc))

        l_stories_pe_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story, max_sent_enc, embed_size))
        l_queries_pe_in = lasagne.layers.InputLayer(shape=(batch_size, 1, max_sent_enc, embed_size))
        # mask the sentences
        l_seq_embed_masks_in = lasagne.layers.InputLayer(shape=(batch_size, max_seq_story))
        # word embedding matrices
        A_embed_W, C_embed_W = lasagne.init.Normal(std=config.normal_std), lasagne.init.Normal(std=config.normal_std)
        A_time_W, C_time_W = lasagne.init.Normal(std=config.normal_std), lasagne.init.Normal(std=config.normal_std)
        # A and B shared the same embedding parameters
        B_embed_W = A_embed_W

        l_queries_in = lasagne.layers.ReshapeLayer(l_queries_in, shape=(batch_size * max_sent_enc, ))
        l_B_embedding = lasagne.layers.EmbeddingLayer(l_queries_in, len(vocab)+1, embed_size, W=B_embed_W,
                                                      name='B_embedding')
        # B.size = (len(vocab)+1, embed_size)
        A_embed_W = l_B_embedding.W

        # reshape the embedding size
        l_B_embedding = lasagne.layers.ReshapeLayer(l_B_embedding, shape=(batch_size, 1, max_sent_enc, embed_size))
        l_B_embedding = lasagne.layers.ElemwiseMergeLayer((l_B_embedding, l_queries_pe_in), merge_function=T.mul)
        l_B_embedding = lasagne.layers.ReshapeLayer(l_B_embedding, shape=(batch_size, max_sent_enc, embed_size))
        l_queries_vec = SumLayer(l_B_embedding, axis=1)
        # initialize the first hop
        self.mem_layers = [SentLevelMemoryLayer((l_stories_in, l_queries_vec, l_stories_pe_in, l_seq_embed_masks_in),
                                                vocab, embed_size, A_embed_W=A_embed_W, A_time_W=A_time_W,
                                                C_embed_W=C_embed_W, C_time_W=C_time_W, non_linearity=self.nonlinearity,
                                                hops_num=0)]
        for hops_idx in range(1, self.num_hops):
            A_embed_W, C_embed_W = self.mem_layers[-1].C_embed_W, lasagne.init.Normal(std=config.normal_std)
            if config.enable_time:
                A_time_W, C_time_W = self.mem_layers[-1].C_time_W, lasagne.init.Normal(std=config.normal_std)

            self.mem_layers += [SentLevelMemoryLayer((l_stories_in, self.mem_layers[-1], l_stories_pe_in,
                                                      l_seq_embed_masks_in), vocab, embed_size, A_embed_W=A_embed_W,
                                                     A_time_W=A_time_W, C_embed_W=C_embed_W, C_time_W=C_time_W,
                                                     non_linearity=self.nonlinearity, hops_num=hops_idx)]

        l_pred_sent_mem = TransposedDenseLayer(self.mem_layers[-1], 1, W=self.mem_layers[-1].C_embed_W,
                                               b=None, nonlinearity=lasagne.nonlinearities.softmax)

        probas_sent_mem = lasagne.layers.get_output(
            l_pred_sent_mem, {l_stories_in: story_texts, l_queries_in: query_texts,
                              l_stories_pe_in: stories_pe, l_queries_pe_in: queries_pe,
                              l_seq_embed_masks_in: seq_embed_masks})
        probas_sent_mem = T.clip(probas_sent_mem, 1e-7, 1.0-1e-7)
        # for word-level memory
        if config.n_hops > 1:
            l_queries_vec = self.mem_layers[-2]
        A_embed_W, C_embed_W = self.mem_layers[-1].A_embed_W, self.mem_layers[-1].C_embed_W
        A_time_W = self.mem_layers[-1].A_time_W
        W_align = lasagne.init.Normal(std=config.normal_std)
        U_align = lasagne.init.Normal(std=config.normal_std)
        v_align = lasagne.init.Normal(std=config.normal_std)
        l_pred_word_mem = WordLevelMemoryLayer((l_queries_vec, l_stories_in, l_stories_pe_in, l_seq_embed_masks_in),
                                               vocab, A_embed_W=A_embed_W, A_time_W=A_time_W, C_embed_W=C_embed_W,
                                               W_align=W_align, U_align=U_align, v_align=v_align,
                                               non_linearity=self.nonlinearity)

        probas_word_mem = lasagne.layers.get_output(
            l_pred_word_mem, {l_stories_in: story_texts, l_queries_in: query_texts,
                              l_stories_pe_in: stories_pe, l_queries_pe_in: queries_pe,
                              l_seq_embed_masks_in: seq_embed_masks})
        probas_word_mem = T.clip(probas_word_mem, 1e-7, 1.0-1e-7)

        cost_sent_mem = T.nnet.categorical_crossentropy(probas_sent_mem, answers).sum()
        params_sent_mem = lasagne.layers.get_all_params(l_pred_sent_mem, trainable=True)
        print 'params_sent_mem:', params_sent_mem
        self.log_file.write('params_sent_mem: ' + str(params_sent_mem) + '\n')
        grads_sent_mem = T.grad(cost_sent_mem, params_sent_mem)
        scaled_grads_sent_mem = lasagne.updates.total_norm_constraint(grads_sent_mem, config.max_norm)
        probas_word_mem_vocab = self.transfer_sub_to_vocab_probas(probas_word_mem, story_texts)
        probas_word_mem_vocab = T.clip(probas_word_mem_vocab, 1e-7, 1.0-1e-7)
        cost_word_mem = T.nnet.categorical_crossentropy(probas_word_mem_vocab, answers).sum()
        params_word_mem = lasagne.layers.get_all_params(l_pred_word_mem, trainable=True)
        print 'params_word_mem:', params_word_mem
        self.log_file.write('params_word_mem: ' + str(params_word_mem) + '\n')
        print 'Start to compile, the process may cost tens of minutes ...'
        self.log_file.write('Start to compile, the process may cost tens of minutes ...' + '\n')
        grads_word_mem = T.grad(cost_word_mem, params_word_mem)
        scaled_grads_word_mem = lasagne.updates.total_norm_constraint(grads_word_mem, config.max_norm)

        scaled_grads_joint, params_joint = self.merge_grads_and_params([scaled_grads_sent_mem,
                                                                        scaled_grads_word_mem],
                                                                       [params_sent_mem, params_word_mem])
        cost_joint = cost_sent_mem + cost_word_mem
        probas_joint = probas_sent_mem + probas_word_mem_vocab
        #
        pred_joint = T.argmax(probas_joint, axis=1)
        pred_sent_mem = T.argmax(probas_sent_mem, axis=1)
        pred_word_mem = T.argmax(probas_word_mem_vocab, axis=1)
        updates_joint = lasagne.updates.sgd(scaled_grads_joint, params_joint, learning_rate=self.lr)
        updates_sent_mem = lasagne.updates.sgd(scaled_grads_sent_mem, params_sent_mem, learning_rate=self.lr)
        updates_word_mem = lasagne.updates.sgd(scaled_grads_word_mem, params_word_mem, learning_rate=self.lr)
        givens = {
            stories: self.stories_shared,
            queries: self.queries_shared,
            answers: self.answers_shared,
            stories_pe: self.stories_pe_shared,
            queries_pe: self.queries_pe_shared,
            seq_embed_masks: self.seq_embed_masks_shared
        }

        self.train_model_joint = theano.function([], [cost_joint, cost_sent_mem, cost_word_mem], givens=givens,
                                                 updates=updates_joint)
        self.train_model_sent_mem = theano.function([], cost_sent_mem, givens=givens, updates=updates_sent_mem,
                                                    on_unused_input='ignore')
        self.train_model_word_mem = theano.function([], cost_word_mem, givens=givens, updates=updates_word_mem,
                                                    on_unused_input='ignore')
        self.compute_pred_joint = theano.function([], outputs=pred_joint, givens=givens, on_unused_input='ignore')
        self.compute_pred_sent_mem = theano.function([], outputs=pred_sent_mem, givens=givens, on_unused_input='ignore')
        self.compute_pred_word_mem = theano.function([], outputs=pred_word_mem, givens=givens, on_unused_input='ignore')

        zero_vec_tensor = T.vector()
        self.zero_vec = np.zeros(embed_size, dtype=theano.config.floatX)
        self.set_zero = theano.function([zero_vec_tensor], updates=[(x, T.set_subtensor(x[0, :], zero_vec_tensor))
                                                                    for x in [A_embed_W]])

        return l_pred_sent_mem

    def transfer_sub_to_vocab_probas(self, probas_word_mem, story_texts):
        # probas_word_mem [batch, seq*sent]
        # story_texts [batch, seq, sent]
        batch_size = config.batch_size
        sub_vocab_size = self.max_sent_enc * self.max_seq_story
        probas_word_mem_vocab = T.zeros((config.batch_size, self.num_classes))
        batch_size_idx = [i for i in range(batch_size)] * sub_vocab_size
        batch_size_idx = np.array(batch_size_idx).reshape((sub_vocab_size, batch_size)).T
        batch_size_idx = batch_size_idx.reshape((sub_vocab_size*batch_size,))
        story_texts_flatten = story_texts.reshape((batch_size*sub_vocab_size,))
        probas_word_mem_vocab = T.set_subtensor(probas_word_mem_vocab[batch_size_idx, story_texts_flatten],
                                                probas_word_mem.reshape((batch_size * sub_vocab_size,)))
        return probas_word_mem_vocab

    def merge_grads_and_params(self, grads_list, params_list):
        param_grad_dict = {}
        for _grads_list, _params_list in zip(grads_list, params_list):
            for _grad, _param in zip(_grads_list, _params_list):
                if _param not in param_grad_dict:
                    param_grad_dict[_param] = _grad
                else:
                    param_grad_dict[_param] += _grad
        return param_grad_dict.values(), param_grad_dict.keys()

    def reset_zero(self):
        self.set_zero(self.zero_vec)
        for _layer in self.mem_layers:
            _layer.reset_zero()

    def predict(self, dataset, index, flag):
        self.set_shared_variables(dataset, index)
        if flag == 'joint':
            result = self.compute_pred_joint()
        elif flag == 'sent_mem':
            result = self.compute_pred_sent_mem()
        else:
            # flag == 'word_mem':
            result = self.compute_pred_word_mem()
        return result

    def compute_f1(self, dataset, flag='joint'):
        n_batches = len(dataset['answers']) // config.batch_size
        y_pred = np.concatenate([self.predict(dataset, i, flag) for i in xrange(n_batches)]).astype(np.int32) - 1
        y_true = [self.vocab.index(y) for y in dataset['answers'][:len(y_pred)]]
        errors = []
        preds = []
        for i, (t, p) in enumerate(zip(y_true, y_pred)):
            if t != p:
                errors.append((i, self.vocab[p]))
                pass
            preds.append(self.vocab[p])
        return metrics.f1_score(y_true, y_pred, average='weighted', pos_label=None), errors, preds

    def train(self, n_epochs=100, shuffle_batch=False):
        epoch = 0
        n_train_batches = len(self.data['train']['answers']) // config.batch_size
        self.lr = self.init_lr
        lowest_dev_err = len(self.data['dev']['answers'])
        lowest_dev_epoch = 0

        while epoch < n_epochs:
            epoch += 1
            if (epoch % config.lrate_decay_step == 0) and (epoch < config.max_decay_step):
                self.lr /= 2.0

            indices = range(n_train_batches)
            if shuffle_batch:
                # synchronously shuffle staries, queries and answers
                self.shuffle_sync(self.data['train'])

            total_cost_joint = 0
            total_cost_sent_mem = 0
            total_cost_word_mem = 0
            start_time = time.time()
            # feed one mini batch
            for minibatch_index in indices:
                # set value to the theano variables
                self.set_shared_variables(self.data['train'], minibatch_index)
                self.reset_zero()
                cost_joint_list = self.train_model_joint()
                total_cost_joint += cost_joint_list[0]
                total_cost_sent_mem += cost_joint_list[1]
                total_cost_word_mem += cost_joint_list[2]

            cost_joint = total_cost_joint / len(indices)
            cost_sent_mem = total_cost_sent_mem / len(indices)
            cost_word_mem = total_cost_word_mem / len(indices)
            end_time = time.time()
            print '\n' * 3, '*' * 80
            self.log_file.write('\n' * 3 + '*' * 80 + '\n')
            print 'Epoch: ', epoch, ', cost_joint:', (cost_joint), \
                ', cost_sent_mem:', (cost_sent_mem), ', cost_word_mem:', (cost_word_mem), \
                ', took: %d(s)' % (end_time - start_time)
            self.log_file.write('epoch:'+str(epoch)+', cost_joint:'+str(cost_joint) +
                                ', cost_sent_mem:'+str(cost_sent_mem) + ', cost_word_mem:' + str(cost_word_mem) +
                                ', took: '+str(end_time - start_time)+'(s)\n')
            print 'TRAIN', '=' * 40
            self.log_file.write('TRAIN' + '=' * 40 + '\n')
            flag = 'joint'
            train_f1, train_errors, train_preds = self.compute_f1(self.data['train'], flag)
            print 'train_f1:', train_f1*100
            self.log_file.write('train_f1:' + str(train_f1*100) + '\n')

            ''' Dev '''
            print 'DEV', '=' * 40
            self.log_file.write('DEV' + '=' * 40 + '\n')

            flag = 'sent_mem'
            dev_f1, dev_errors_sent_mem, dev_preds_sent_mem = self.compute_f1(self.data['dev'], flag)
            print 'dev_f1_sent_mem, dev_errors_sent_mem: ', dev_f1, ', ', len(dev_errors_sent_mem)
            self.log_file.write('dev_f1_sent_mem, dev_errors_sent_mem: ' + str(dev_f1) + ', ' +
                                str(len(dev_errors_sent_mem)) + '\n')
            flag = 'word_mem'
            dev_f1, dev_errors_word_mem, dev_preds_word_mem = self.compute_f1(self.data['dev'], flag)
            print 'dev_f1_word_mem, dev_errors_word_mem: ', dev_f1, ', ', len(dev_errors_word_mem)
            self.log_file.write('dev_f1_word_mem, dev_errors_word_mem: ' + str(dev_f1) + ', ' +
                                str(len(dev_errors_word_mem)) + '\n')
            flag = 'joint'
            dev_f1, dev_errors, dev_preds = self.compute_f1(self.data['dev'], flag)
            print 'dev_f1_joint, dev_errors_joint: ', dev_f1, ', ', len(dev_errors)
            self.log_file.write('dev_f1_joint, dev_errors_joint: ' + str(dev_f1) + ', ' +
                                str(len(dev_errors)) + '\n')

            ''' Test '''
            print 'TEST', '=' * 40
            self.log_file.write('TEST' + '=' * 40 + '\n')
            flag = 'sent_mem'
            test_f1, test_errors_sent_mem, test_preds_sent_mem = self.compute_f1(self.data['test'], flag)
            print 'test_f1_sent_mem, test_errors_sent_mem: ', test_f1, ', ', len(test_errors_sent_mem)
            self.log_file.write('test_f1_sent_mem, test_errors_sent_mem: ' + str(test_f1) + ', ' +
                                str(len(test_errors_sent_mem)) + '\n')
            flag = 'word_mem'
            test_f1, test_errors_word_mem, test_preds_word_mem = self.compute_f1(self.data['test'], flag)
            print 'test_f1_word_mem, test_errors_word_mem: ', test_f1, ', ', len(test_errors_word_mem)
            self.log_file.write('test_f1_word_mem, test_errors_word_mem: ' + str(test_f1) + ', ' +
                                str(len(test_errors_word_mem)) + '\n')
            flag = 'joint'
            test_f1, test_errors, test_preds = self.compute_f1(self.data['test'], flag)
            print 'test_f1_joint, test_errors_joint: ', test_f1, ', ', len(test_errors)
            self.log_file.write('test_f1_joint, test_errors_joint: ' + str(test_f1) + ', ' +
                                str(len(test_errors)) + '\n')

            if len(dev_errors) < lowest_dev_err:
                lowest_dev_err = len(dev_errors)
                lowest_dev_epoch = epoch
            else:
                if (epoch - lowest_dev_epoch) >= config.stop_iter_dev:
                    print 'Stop the iteration by dev evaluation.'
                    self.log_file.write('Stop the iteration by dev evaluation.' + '\n')
                    self.log_file.flush()
                    break
            self.log_file.flush()

    def set_shared_variables(self, dataset, index):
        stories = np.zeros((config.batch_size, self.max_seq_story), dtype=np.int32)
        queries = np.zeros((config.batch_size, ), dtype=np.int32)
        answers = np.zeros((config.batch_size, self.num_classes), dtype=np.int32)
        stories_pe = np.zeros((config.batch_size, self.max_seq_story, self.max_sent_enc, self.embedding_size),
                              dtype=theano.config.floatX)
        queries_pe = np.zeros((config.batch_size, 1, self.max_sent_enc, self.embedding_size),
                              dtype=theano.config.floatX)
        stories_seq_embed_masks = np.zeros((config.batch_size, self.max_seq_story, self.embedding_size),
                                           dtype=theano.config.floatX)
        stories_seq_masks = np.zeros((config.batch_size, self.max_seq_story),
                                     dtype=theano.config.floatX)
        indices = range(index*config.batch_size, (index+1)*config.batch_size)
        for sample_idx, row in enumerate(dataset['stories'][indices]):
            row = row[:self.max_seq_story]
            stories[sample_idx, :len(row)] = row
        queries[:len(indices)] = dataset['queries'][indices]

        for key, mask in [('stories', stories_pe), ('queries', queries_pe)]:
            for sample_idx, row in enumerate(dataset[key][indices]):
                sentences = self.all_text_idx[row].reshape((-1, self.max_sent_enc))
                if key == 'stories':
                    for seq_idx in np.nonzero(np.sum(sentences, axis=1)):
                        stories_seq_embed_masks[sample_idx, seq_idx, :] = 1
                        stories_seq_masks[sample_idx, seq_idx] = 1
                for sent_idx, word_list_idx in enumerate(sentences):
                    J = np.count_nonzero(word_list_idx)
                    for j in np.arange(J):
                        mask[sample_idx, sent_idx, j, :] = (1 - (j+1)/J) - \
                                            ((np.arange(self.embedding_size)+1)/self.embedding_size)*(1 - 2*(j+1)/J)

        answers[:len(indices), 1:self.num_classes] = label_binarize(dataset['answers'][indices], self.vocab)
        self.stories_shared.set_value(stories)
        self.queries_shared.set_value(queries)
        self.answers_shared.set_value(answers)
        self.stories_pe_shared.set_value(stories_pe)
        self.queries_pe_shared.set_value(queries_pe)
        self.seq_embed_masks_shared.set_value(stories_seq_embed_masks)
