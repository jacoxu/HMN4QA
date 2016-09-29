# <-*- encoding: utf-8 -*->
"""
    pre-process data
"""

import config
import numpy as np
import re
import glob
__author__ = 'jacoxu & shin'


def get_vocab(lines):

    vocab = set()
    max_sent_enc = 0
    max_sent_dec = 0
    for line_idx, line in enumerate(lines):
        words = tokenize(line['text'])
        max_sent_enc = max(max_sent_enc, len(words))
        for w in words:
            vocab.add(w)
        if line['type'] == 'query':
            words = [line['answer']]
            max_sent_dec = max(max_sent_dec, len(words))
            for w in words:
                vocab.add(w)
    # adjust to the true length
    max_sent_enc = max_sent_enc if max_sent_enc < config.max_sent_enc else config.max_sent_enc
    max_sent_dec = max_sent_dec if max_sent_dec < config.max_sent_dec else config.max_sent_dec

    word_to_idx = {}
    # the first index 0 is used for mask
    for w in vocab:
        word_to_idx[w] = len(word_to_idx) + 1
    idx_to_word = {}
    for w, idx in word_to_idx.iteritems():
        idx_to_word[idx] = w

    vocab = []
    for idx in range(len(idx_to_word)):
        vocab.append(idx_to_word[idx+1])
    max_seq_story = 0
    for line_idx, line in enumerate(lines):
        if line['type'] == 'query':
            nid = line['id']-1
            indices = [idx for idx in range(line_idx-nid, line_idx)
                       if lines[idx]['type'] == 'story'][::-1][:config.max_seq_story]
            max_seq_story = max(len(indices), max_seq_story)
            max_seq_story = max_seq_story if max_seq_story < config.max_seq_story else config.max_seq_story

    return vocab, word_to_idx, idx_to_word, max_seq_story, max_sent_enc, max_sent_dec


def process_dataset(lines, word_to_idx, max_sent_enc, offset):
    text_idx, stories, queries, answers = [], [], [], []
    for line_idx, line in enumerate(lines):
        word_indices = [word_to_idx[w] for w in tokenize(line['text'])]
        # fill 0 until max_sentLen
        word_indices += [0] * (max_sent_enc - len(word_indices))
        text_idx.append(word_indices)
        if line['type'] == 'query':
            nid = line['id']-1
            indices = [offset+idx+1 for idx in range(line_idx-nid, line_idx)
                       if lines[idx]['type'] == 'story'][::-1][:config.max_seq_story]
            stories.append(indices)
            queries.append(offset+line_idx+1)
            answers.append(line['answer'])
    return np.array(text_idx, dtype=np.int32), np.array(stories), np.array(queries, dtype=np.int32), \
            np.array(answers)


def get_lines(data_files):
    lines = []
    for file_idx, _fp in enumerate(glob.glob(data_files)):
        for line_idx, line in enumerate(open(_fp)):
            line = line.strip()
            nid, line = line.split(' ', 1)
            nid = int(nid)
            # if not query line
            if '\t' not in line:
                lines.append({'type': 'story', 'text': line})
            else:
                # if query line
                tmp_str = line.split('\t')
                if len(tmp_str) >= 3:
                    if tmp_str[0].strip().endswith('?') or tmp_str[0].strip().endswith('？'):
                        query_text = tmp_str[0].strip()[:-1].strip()
                    else:
                        query_text = tmp_str[0].strip()
                    lines.append({'id': nid, 'type': 'query', 'text': query_text, 'answer': tmp_str[1].strip()
                                 , 'refs': [int(x) for x in tmp_str[2].strip().split(' ')]})
                else:
                    lines.append({'id': nid, 'type': 'query', 'text': tmp_str[0].strip(), 'answer': tmp_str[1].strip()
                                 , 'refs': []})

        # if input file too much, it's must bug.
        if file_idx > 1000:
            print ('The input files size is %d, should check it.' % len(glob.glob(data_files)))
            break
    return np.array(lines)


def tokenize(sent):
    """
        Return the tokens of a sentence including punctuation.
        :param sent
        tokenize('Bob dropped the apple. Where is the apple?')
        ['Bob', 'dropped', 'the', 'apple', '.', 'Where', 'is', 'the', 'apple', '?']
    """
    if config.is_blank_split:
        return [x.strip() for x in sent.split(' ') if x.strip()]
    else:
        return [x.strip() for x in re.split('(\W+)?', sent) if x.strip()]
