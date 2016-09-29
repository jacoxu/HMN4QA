# -*- coding: utf-8 -*-
"""
    Initialize the parameters of model
"""
import config
from sklearn.preprocessing import LabelBinarizer
import prepare_data
import numpy as np
import theano
import theano.tensor as T
__author__ = 'jacoxu & shin'


class ModelInit(object):

    def __init__(self, _log_file):
        # pre-process data
        print("Start to prepare data set")
        train_data_path = config.data_path.format('train')
        dev_data_path = config.data_path.format('dev')
        test_data_path = config.data_path.format('test')
        train_lines, dev_lines, test_lines = prepare_data.get_lines(train_data_path), \
                                             prepare_data.get_lines(dev_data_path), \
                                             prepare_data.get_lines(test_data_path)

        all_lines = np.concatenate([train_lines, dev_lines, test_lines], axis=0)
        vocab, word_to_idx, idx_to_word, max_seq_story, max_sent_enc, max_resp_dec = prepare_data.get_vocab(all_lines)

        self.data = {'train': {}, 'dev': {}, 'test': {}}
        text_idx_train, self.data['train']['stories'], self.data['train']['queries'], self.data['train']['answers'] = \
            prepare_data.process_dataset(train_lines, word_to_idx, max_sent_enc, offset=0)
        text_idx_dev, self.data['dev']['stories'], self.data['dev']['queries'], self.data['dev']['answers'] = \
            prepare_data.process_dataset(dev_lines, word_to_idx, max_sent_enc, offset=len(text_idx_train))
        text_idx_test, self.data['test']['stories'], self.data['test']['queries'], self.data['test']['answers'] = \
            prepare_data.process_dataset(test_lines, word_to_idx, max_sent_enc, offset=(len(text_idx_train) +
                                                                                        len(text_idx_dev)))
        all_text_idx = np.concatenate([np.zeros((1, max_sent_enc), dtype=np.int32),
                                       text_idx_train, text_idx_dev, text_idx_test], axis=0)
        for sample_idx in range(min(3, len(self.data['test']['stories']))):
            print '-' * 80
            for type_idx in ['stories', 'queries', 'answers']:
                print 'Test sample', str(sample_idx), ': ', type_idx, self.data['test'][type_idx][sample_idx]
        print '-' * 80
        print 'batch_size:', config.batch_size, 'max_seq_story:', max_seq_story, 'max_sent_enc:', max_sent_enc
        print 'all_text_idx:', all_text_idx.shape
        print 'vocab size:', len(vocab)

        for data_type in ['train', 'dev', 'test']:
            print data_type,
            for type_idx in ['stories', 'queries', 'answers']:
                print type_idx, self.data[data_type][type_idx].shape,
            print ''

        label_binarizer = LabelBinarizer()

        self.max_seq_story = max_seq_story
        self.max_sent_enc = max_sent_enc if config.enable_time else max_sent_enc+1
        self.embedding_size = config.embed_size

        self.num_classes = len(vocab) + 1
        self.vocab = vocab
        self.num_hops = config.n_hops
        self.label_binarizer = label_binarizer
        self.init_lr = config.init_lr
        self.lr = self.init_lr
        self.all_text_idx = all_text_idx
        self.idx_to_word = idx_to_word
        self.nonlinearity = None
        self.word_to_idx = word_to_idx

        # [batch_size, max_seq_story, max_sent_enc]
        self.stories = T.imatrix('stories')
        self.queries = T.ivector('queries')
        self.answers = T.imatrix('answers')
        # position encoding (pe)
        # [batch_size, max_seq_story, max_sent_enc, embed_size]
        self.stories_pe = T.tensor4('stories_pe')
        self.queries_pe = T.tensor4('queries_pe')
        # seq_mask for stories [batch_size, max_seq_story]
        self.seq_masks = T.tensor3('seq_masks')

        self.stories_shared = theano.shared(np.zeros((config.batch_size, max_seq_story), dtype=np.int32), borrow=True)
        self.queries_shared = theano.shared(np.zeros((config.batch_size,), dtype=np.int32), borrow=True)
        self.answers_shared = theano.shared(np.zeros((config.batch_size, self.num_classes),
                                                     dtype=np.int32), borrow=True)

        self.stories_pe_shared = theano.shared(np.zeros((config.batch_size, max_seq_story, max_sent_enc,
                                                         config.embed_size), dtype=theano.config.floatX), borrow=True)
        self.queries_pe_shared = theano.shared(np.zeros((config.batch_size, 1, max_sent_enc, config.embed_size),
                                                        dtype=theano.config.floatX), borrow=True)

        self.seq_embed_masks_shared = theano.shared(np.zeros((config.batch_size, max_seq_story, config.embed_size),
                                                             dtype=theano.config.floatX), borrow=True)

        all_text_idx_shared = theano.shared(self.all_text_idx, borrow=True)

        self.story_texts = all_text_idx_shared[self.stories.flatten()].reshape((config.batch_size, max_seq_story,
                                                                                max_sent_enc))
        self.query_texts = all_text_idx_shared[self.queries.flatten()].reshape((config.batch_size, max_sent_enc))

    def to_words(self, indices):
        sents = []
        for idx in indices:
            words = ' '.join([self.idx_to_word[idx] for idx in self.all_text_idx[idx] if idx > 0])
            sents.append(words)
        return ' '.join(sents)

    def shuffle_sync(self, dataset):
        p = np.random.permutation(len(dataset['answers']))
        for k in ['stories', 'queries', 'answers']:
            dataset[k] = dataset[k][p]
