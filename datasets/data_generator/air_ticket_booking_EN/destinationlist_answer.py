# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

destinationlist_answer = []
destinationlist_answer.append('Beijing')
destinationlist_answer.append('Beijing')
destinationlist_answer.append('Beijing')
destinationlist_answer.append('Beijing .')
destinationlist_answer.append('Beijing .')
destinationlist_answer.append('Beijing .')

destinationlist_answer.append('go to Beijing')
destinationlist_answer.append('the destination city is Beijing .')
destinationlist_answer.append('flight to Beijing .')
destinationlist_answer.append('is Beijing .')
destinationlist_answer.append('go to Beijing .')
destinationlist_answer.append('to Beijing .')
destinationlist_answer.append('Beijing is my destination')
destinationlist_answer.append('the destination is Beijing')
destinationlist_answer.append('i want go to Beijing')
destinationlist_answer.append('plane for Beijing .')
destinationlist_answer.append('buy a ticket to Beijing .')
destinationlist_answer.append('i want to book a flight to Beijing')
destinationlist_answer.append('i need to fly to Beijing')

destinationlist_answer.append('going to Beijing')
destinationlist_answer.append('i\'m leaving for Beijing')
destinationlist_answer.append('ticket to Beijing')
destinationlist_answer.append('air ticket to Beijing .')
destinationlist_answer.append('my final destination is Beijing .')

destinationlist_answer_split = []

for ans in destinationlist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('Beijing', '[slot_destination]')
    destinationlist_answer_split.append(w_sent)
pass
