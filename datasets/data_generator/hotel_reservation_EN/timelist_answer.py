# -*- coding: utf8 -*-
__author__ = 'shin'

timelist_answer = []

timelist_answer.append('tomorrow')
timelist_answer.append('tomorrow')
timelist_answer.append('tomorrow')

timelist_answer.append('tomorrow .')
timelist_answer.append('tomorrow .')
timelist_answer.append('tomorrow .')

timelist_answer.append('i want to arrive on tomorrow .')
timelist_answer.append('i want to check in on tomorrow .')
timelist_answer.append('i am making a reservation for tomorrow')
timelist_answer.append('i need a reservation on tomorrow')
timelist_answer.append('i\'d like to check in on tomorrow')
timelist_answer.append('check in time is tomorrow .')
timelist_answer.append('book a hotel on tomorrow .')
timelist_answer.append('i will check in on tomorrow .')
timelist_answer.append('i will arrive on tomorrow .')
timelist_answer.append('tomorrow is ok .')
timelist_answer.append('need to check in on tomorrow .')
timelist_answer.append('i\'d like to book a hotel on tomorrow .')
timelist_answer.append('please reserve the hotel on tomorrow .')
timelist_answer.append('uh , the arrival time is tomorrow .')

timelist_answer.append('the arrival date is tomorrow .')
timelist_answer.append('the date is tomorrow .')
timelist_answer.append('i plan to check in on tomorrow .')
timelist_answer.append('i want to arrive on tomorrow .')
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
