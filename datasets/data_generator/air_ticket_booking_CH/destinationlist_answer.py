# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

destinationlist_answer = []

destinationlist_answer.append('北京')
destinationlist_answer.append('北京')
destinationlist_answer.append('北京')
destinationlist_answer.append('北京。')
destinationlist_answer.append('北京。')
destinationlist_answer.append('北京。')

destinationlist_answer.append('去北京。')
destinationlist_answer.append('目的地是北京。')
destinationlist_answer.append('飞往北京。')
destinationlist_answer.append('是北京。')
destinationlist_answer.append('去北京。')
destinationlist_answer.append('往北京。')
destinationlist_answer.append('到北京去。')
destinationlist_answer.append('北京是我的目的地。')
destinationlist_answer.append('目的地是北京。')
destinationlist_answer.append('我要到北京去。')
destinationlist_answer.append('飞往北京的飞机。')
destinationlist_answer.append('买去北京的机票。')
destinationlist_answer.append('我要订去北京的飞机。')

destinationlist_answer.append('我要去北京')
destinationlist_answer.append('到北京')
destinationlist_answer.append('我到北京')
destinationlist_answer.append('我去北京')
destinationlist_answer.append('到北京的机票')
destinationlist_answer.append('飞北京的机票')
destinationlist_answer.append('到北京的票')
destinationlist_answer.append('飞北京的票')
destinationlist_answer.append('去北京的机票')
destinationlist_answer.append('去北京的票')

destinationlist_answer_split = []

for ans in destinationlist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('北京'.decode('utf8'), '[slot_destination]')
    destinationlist_answer_split.append(w_sent)
pass
