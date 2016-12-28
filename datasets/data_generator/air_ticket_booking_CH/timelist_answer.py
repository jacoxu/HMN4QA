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
timelist_answer.append('帮我预订明天的机票。')
timelist_answer.append('出行时间是明天。')
timelist_answer.append('订明天的机票。')
timelist_answer.append('明天走。')
timelist_answer.append('明天出发。')
timelist_answer.append('明天之前。')
timelist_answer.append('在明天出发就行。')
timelist_answer.append('需要明天出发。')
timelist_answer.append('我要订明天的飞机。')
timelist_answer.append('订购明天的机票。')
timelist_answer.append('出行时间应该是明天。')
timelist_answer.append('于明天出行。')
timelist_answer.append('在明天走。')

timelist_answer.append('明天出发')
timelist_answer.append('明天走')
timelist_answer.append('出发时间明天')
timelist_answer.append('时间明天')
timelist_answer.append('我打算明天出发')
timelist_answer.append('我想明天出发')
timelist_answer.append('明天出发的票')
timelist_answer.append('明天出发的机票')
timelist_answer.append('明天走的票')
timelist_answer.append('明天走的机票')
timelist_answer.append('明天的机票')
timelist_answer.append('明天的票')


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
