# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

countlist_answer = []
countlist_answer.append('one room')
countlist_answer.append('one room')
countlist_answer.append('one')
countlist_answer.append('one room .')
countlist_answer.append('one room .')
countlist_answer.append('one .')
countlist_answer.append('i need one room .')
countlist_answer.append('i want to book one room .')
countlist_answer.append('booking one room please .')
countlist_answer.append('the number of rooms is one .')
countlist_answer.append('i want to reserve one room .')
countlist_answer.append('please help me to book one room .')
countlist_answer.append('one hotel room .')

countlist_answer.append('one hotel room')
countlist_answer.append('i want to reserve one')
countlist_answer.append('please help me to book one .')
countlist_answer.append('reserve one room for me , please .')
countlist_answer.append('reserve one please .')

countlist_answer_split = []
for ans in countlist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('one', '[slot_count]')
    countlist_answer_split.append(w_sent)
pass
