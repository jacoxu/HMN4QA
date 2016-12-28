# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

timelist_answer = []
timelist_answer.append('tomorrow')
timelist_answer.append('tomorrow')
timelist_answer.append('tomorrow')

timelist_answer.append('tomorrow .')
timelist_answer.append('tomorrow .')
timelist_answer.append('tomorrow .')

timelist_answer.append('i want to fly on tomorrow .')
timelist_answer.append('i want to fly on tomorrow .')
timelist_answer.append('i am making a reservation for tomorrow')
timelist_answer.append('i need a flight on tomorrow')
timelist_answer.append('i\'d like to go on tomorrow')
timelist_answer.append('travel time is tomorrow .')
timelist_answer.append('book a ticket on tomorrow .')
timelist_answer.append('i will leave on tomorrow .')
timelist_answer.append('i will go on tomorrow .')
timelist_answer.append('tomorrow is ok .')
timelist_answer.append('need to leave on tomorrow .')
timelist_answer.append('i\'d like to book a flight on tomorrow .')
timelist_answer.append('please reserve the ticket on tomorrow .')
timelist_answer.append('uh , the travel time is tomorrow .')

timelist_answer.append('the travel date is tomorrow .')
timelist_answer.append('the date is tomorrow .')
timelist_answer.append('i plan to leave on tomorrow .')
timelist_answer.append('i want to go on tomorrow .')
timelist_answer.append('on tomorrow .')

timelist_answer_split = []
for ans in timelist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('tomorrow', '[slot_time]')
    timelist_answer_split.append(w_sent)

pass
