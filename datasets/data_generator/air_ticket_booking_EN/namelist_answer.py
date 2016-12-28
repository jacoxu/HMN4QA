# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

namelist_answer = []
namelist_answer.append('John')
namelist_answer.append('John')
namelist_answer.append('John')

namelist_answer.append('John .')
namelist_answer.append('John .')
namelist_answer.append('John .')

namelist_answer.append('is John .')
namelist_answer.append('name is John .')
namelist_answer.append('i am John .')
namelist_answer.append('yeah , i am John .')
namelist_answer.append('my name is John .')
namelist_answer.append('uh , my name is John .')
namelist_answer.append('my name is John')
namelist_answer.append('the name is John .')
namelist_answer.append('call me John')
namelist_answer.append('sure , i am John')
namelist_answer.append('ok , name is John')
namelist_answer.append('my full name is John')
namelist_answer.append('name is John')
namelist_answer.append('John is my name')
namelist_answer.append('i\'m John')
namelist_answer.append('ah , my name is John .')
namelist_answer.append('hi , my name is John .')
namelist_answer.append('ok , John')

namelist_answer_split = []
for ans in namelist_answer:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('John', '[slot_name]')
    namelist_answer_split.append(w_sent)
pass
