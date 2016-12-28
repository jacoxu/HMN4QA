# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

phonelist_answer=[]
phonelist_answer.append('001')
phonelist_answer.append('001')
phonelist_answer.append('001')

phonelist_answer.append('001 .')
phonelist_answer.append('001 .')
phonelist_answer.append('001 .')
phonelist_answer.append('the number is 001')
phonelist_answer.append('001 is my phone number .')
phonelist_answer.append('the phone number 001')
phonelist_answer.append('the phone number is 001 .')
phonelist_answer.append('the phone number 001 .')
phonelist_answer.append('001 is my phone number .')
phonelist_answer.append('uh , 001')
phonelist_answer.append('uh ，is 001 .')
phonelist_answer.append('ah , 001')
phonelist_answer.append('yeah , my phone number is 001 .')
phonelist_answer.append('my phone number would be 001')
phonelist_answer.append('my phone number is 001 .')
phonelist_answer.append('is 001 .')
phonelist_answer.append('the phone number is 001')
phonelist_answer.append('my cell number is 001')

phonelist_answer.append('my contact number is 001')
phonelist_answer.append('hmm , my phone number is 001')
phonelist_answer.append('my contact number 001')
phonelist_answer.append('contact number 001')
phonelist_answer.append('001 , that is my contact number .')
phonelist_answer.append('001 , my phone number .')

phonelist_answer_split = []
for ans in phonelist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('001', '[slot_phone]')
    phonelist_answer_split.append(w_sent)
pass
