# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

phonelist_answer=[]
phonelist_answer.append('秘密')
phonelist_answer.append('秘密')
phonelist_answer.append('秘密')

phonelist_answer.append('秘密。')
phonelist_answer.append('秘密。')
phonelist_answer.append('秘密。')
phonelist_answer.append('号码秘密。')
phonelist_answer.append('秘密我的号码。')
phonelist_answer.append('电话号秘密。')
phonelist_answer.append('电话号码码是秘密。')
phonelist_answer.append('电话号码秘密。')
phonelist_answer.append('秘密是我的电话号。')
phonelist_answer.append('等我想想。秘密。')
phonelist_answer.append('额，是秘密。')
phonelist_answer.append('啊，秘密。')
phonelist_answer.append('知道了，我的电话号码是秘密。')
phonelist_answer.append('号码应该是秘密。')
phonelist_answer.append('我的电话号码是秘密。')
phonelist_answer.append('是秘密。')
phonelist_answer.append('电话号码是秘密。')
phonelist_answer.append('我的电话号是秘密。')

phonelist_answer.append('我的电话号码是秘密')
phonelist_answer.append('号码是秘密')
phonelist_answer.append('你记一下，秘密')
phonelist_answer.append('我的电话是秘密')
phonelist_answer.append('我的电话秘密')
phonelist_answer.append('电话秘密')
phonelist_answer.append('你记一下我的号码秘密')
phonelist_answer.append('请记一下我的电话号码秘密')
phonelist_answer.append('秘密，这是我的号码')
phonelist_answer.append('秘密，我的号码')

phonelist_answer_split = []
for ans in phonelist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('秘密'.decode('utf8'), '[slot_phone]')
    phonelist_answer_split.append(w_sent)
pass
