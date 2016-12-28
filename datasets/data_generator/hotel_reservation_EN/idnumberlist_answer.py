# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

idnumberlist_answer = []
idnumberlist_answer.append('001')
idnumberlist_answer.append('001')
idnumberlist_answer.append('001')

idnumberlist_answer.append('001 .')
idnumberlist_answer.append('001 .')
idnumberlist_answer.append('001 .')
idnumberlist_answer.append('the number 001')
idnumberlist_answer.append('001 is my number .')
idnumberlist_answer.append('the passport number 001')
idnumberlist_answer.append('the passport number is 001 .')
idnumberlist_answer.append('ok , the number is 001 .')
idnumberlist_answer.append('001 is my passport number .')
idnumberlist_answer.append('uh , 001')
idnumberlist_answer.append('ok , my passport number is 001')
idnumberlist_answer.append('the number is 001 .')

idnumberlist_answer.append('my passport number is 001 .')
idnumberlist_answer.append('is 001')
idnumberlist_answer.append('uh , is 001 .')
idnumberlist_answer.append('ah , is 001 .')

idnumberlist_answer.append('the number is 001')
idnumberlist_answer.append('001 , that is my number .')
idnumberlist_answer.append('001 , my passport number .')

idnumberlist_answer_split = []
for ans in idnumberlist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('001', '[slot_idnumber]')
    idnumberlist_answer_split.append(w_sent)
pass
