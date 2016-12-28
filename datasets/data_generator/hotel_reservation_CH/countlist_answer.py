# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'
import jieba

countlist_answer = []
countlist_answer.append('一张')
countlist_answer.append('一张')
countlist_answer.append('一张')
countlist_answer.append('一张。')
countlist_answer.append('一张。')
countlist_answer.append('一张。')
countlist_answer.append('一张就够了。')
countlist_answer.append('我要一张房间。')
countlist_answer.append('我想订一张。')
countlist_answer.append('订一张票就可以。')
countlist_answer.append('房间数量是一张。')
countlist_answer.append('想预订一张房间。')
countlist_answer.append('一张即可。')
countlist_answer.append('可能需要一张。')
countlist_answer.append('一张就可以了。')
countlist_answer.append('帮我预订一张。')
countlist_answer.append('一张房间。')

countlist_answer.append('一张房')
countlist_answer.append('一张房间')
countlist_answer.append('我要订一张房')
countlist_answer.append('我要订一张房间')
countlist_answer.append('帮我订一张')
countlist_answer.append('预订一张')
countlist_answer.append('请帮我预订一张')

countlist_answer_split = []

for ans in countlist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('一张'.decode('utf8'), '[slot_count]')
    countlist_answer_split.append(w_sent)
pass
