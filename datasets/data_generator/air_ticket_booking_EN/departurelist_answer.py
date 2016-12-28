# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

departurelist_answer = []
departurelist_answer.append('Beijing')
departurelist_answer.append('Beijing')
departurelist_answer.append('Beijing')
departurelist_answer.append('uh , Beijing')
departurelist_answer.append('Beijing .')
departurelist_answer.append('Beijing .')
departurelist_answer.append('Beijing .')
departurelist_answer.append('ah , is Beijing .')

departurelist_answer.append('take off from Beijing .')
departurelist_answer.append('flight from Beijing')
departurelist_answer.append('ticket starting in Beijing .')
departurelist_answer.append('starting in Beijing .')
departurelist_answer.append('from Beijing .')
departurelist_answer.append('the flight taking off from Beijing .')
departurelist_answer.append('the departure is Beijing .')
departurelist_answer.append('help me book a flight to Beijing takes off .')
departurelist_answer.append('book a flight from Beijing .')

departurelist_answer.append('i start from Beijing')
departurelist_answer.append('departure from Beijing')
departurelist_answer.append('my departure city is Beijing')
departurelist_answer.append('i plan to start from Beijing .')
departurelist_answer.append('i will start from Beijing .')
departurelist_answer.append('i may start from Beijing')
departurelist_answer.append('i\'m going to start from Beijing .')
departurelist_answer.append('my departure is Beijing')

departurelist_answer_split = []

for ans in departurelist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('Beijing', '[slot_departure]')
    departurelist_answer_split.append(w_sent)
pass
