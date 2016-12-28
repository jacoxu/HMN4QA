# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

timelist_answer=[]

timelist_answer.append('明天')
timelist_answer.append('明天')
timelist_answer.append('明天')

timelist_answer.append('明天。')
timelist_answer.append('明天。')
timelist_answer.append('明天。')

timelist_answer.append('时间是明天。')
timelist_answer.append('帮我预订明天的宾馆。')
timelist_answer.append('入住时间是明天。')
timelist_answer.append('订明天的房间。')
timelist_answer.append('明天住。')
timelist_answer.append('明天入住。')
timelist_answer.append('明天左右。')
timelist_answer.append('在明天入住就行。')
timelist_answer.append('需要明天入住。')
timelist_answer.append('我要订明天的房间。')
timelist_answer.append('预订明天的宾馆。')
timelist_answer.append('入住时间应该是明天。')
timelist_answer.append('于明天入住。')
timelist_answer.append('在明天住。')

timelist_answer.append('明天入住')
timelist_answer.append('明天住')
timelist_answer.append('入住时间明天')
timelist_answer.append('时间明天')
timelist_answer.append('我打算明天入住')
timelist_answer.append('我想明天入住')
timelist_answer.append('明天入住的宾馆')
timelist_answer.append('明天入住的房间')
timelist_answer.append('明天住的房间')
timelist_answer.append('明天住的宾馆')
timelist_answer.append('明天的房间')
timelist_answer.append('明天的宾馆')


timelist_answer_split = []
for ans in timelist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('明天'.decode('utf8'), '[slot_time]')
    timelist_answer_split.append(w_sent)

pass
