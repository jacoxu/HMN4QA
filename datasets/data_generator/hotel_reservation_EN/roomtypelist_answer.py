# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

roomtpyelist_answer = []

roomtpyelist_answer.append('single')
roomtpyelist_answer.append('single')
roomtpyelist_answer.append('single room')
roomtpyelist_answer.append('uh , single')
roomtpyelist_answer.append('single .')
roomtpyelist_answer.append('single .')
roomtpyelist_answer.append('single room .')
roomtpyelist_answer.append('ah , need single room .')

roomtpyelist_answer.append('book single room')
roomtpyelist_answer.append('reserve single room')
roomtpyelist_answer.append('i want to book single')
roomtpyelist_answer.append('i want to reserve single room .')
roomtpyelist_answer.append('single room is ok .')
roomtpyelist_answer.append('single')
roomtpyelist_answer.append('single room is okey .')
roomtpyelist_answer.append('single is ok .')
roomtpyelist_answer.append('booking the single room is ok .')
roomtpyelist_answer.append('room type is single .')
roomtpyelist_answer.append('please help me to book the single room .')
roomtpyelist_answer.append('help me to reserve the single room .')

roomtpyelist_answer.append('i plan to book the single room .')
roomtpyelist_answer.append('i need the single room .')
roomtpyelist_answer.append('i want to book the single room .')
roomtpyelist_answer.append('i need to book the single room .')
roomtpyelist_answer.append('uh , help me to book the single room .')
roomtpyelist_answer.append('reserve the single room , thanks .')

roomtypelist_answer_split = []

for ans in roomtpyelist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('single', '[slot_roomtype]')
    roomtypelist_answer_split.append(w_sent)
pass
