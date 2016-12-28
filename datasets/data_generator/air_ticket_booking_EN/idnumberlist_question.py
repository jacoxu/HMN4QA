# -*- coding: utf8 -*-

__author__ = 'shin & jacoxu'

idnumberlist_question_female = []
idnumberlist_question_female.append('miss , may i have your passport number , please ?')
idnumberlist_question_female.append('may i have your passport number , miss .')
idnumberlist_question_female.append('miss , your passport number , please .')
idnumberlist_question_female.append('please tell me your passport number , miss .')
idnumberlist_question_female.append('hello miss , i need your passport number .')
idnumberlist_question_female.append('hello miss , i need the passport number .')
idnumberlist_question_female.append('please tell me the passport number , miss .')
idnumberlist_question_female.append('please tell me the passenger\'s passport number , miss .')
idnumberlist_question_female.append('miss , the passenger\'s passport number is ?')
idnumberlist_question_female.append('what is your passport number , miss ?')
idnumberlist_question_female.append('we need to known your passport number , miss .')
idnumberlist_question_female.append('passport number , miss ?')
idnumberlist_question_female.append('miss , passport number , please .')
idnumberlist_question_female.append('miss , need your passport number , thanks .')
idnumberlist_question_female.append('miss , passport number , thanks .')
idnumberlist_question_female.append('could you tell me the passport number , miss ?')
idnumberlist_question_female.append('ok miss , please tell me your passport number , thanks very much .')
idnumberlist_question_female.append('ok miss , your passport number ?')
idnumberlist_question_female.append('get it , what is your passport number , miss ?')
idnumberlist_question_female.append('i see , please tell me your passport number , miss .')
idnumberlist_question_female.append('well miss , your passport number , please .')

idnumberlist_question_male = []
idnumberlist_question_male.append('sir , may i have your passport number , please ?')
idnumberlist_question_male.append('may i have your passport number , sir .')
idnumberlist_question_male.append('sir , your passport number , please .')
idnumberlist_question_male.append('please tell me your passport number , sir .')
idnumberlist_question_male.append('hello sir , i need your passport number .')
idnumberlist_question_male.append('hello sir , i need the passport number .')
idnumberlist_question_male.append('please tell me the passport number , sir .')
idnumberlist_question_male.append('please tell me the passenger\'s passport number , sir .')
idnumberlist_question_male.append('sir , the passenger\'s passport number is ?')
idnumberlist_question_male.append('what is your passport number , sir ?')
idnumberlist_question_male.append('we need to known your passport number , sir .')
idnumberlist_question_male.append('passport number , sir ?')
idnumberlist_question_male.append('sir , passport number , please .')
idnumberlist_question_male.append('sir , need your passport number , thanks .')
idnumberlist_question_male.append('sir , passport number , thanks .')
idnumberlist_question_male.append('could you tell me the passport number , sir ?')
idnumberlist_question_male.append('ok sir , please tell me your passport number , thanks very much .')
idnumberlist_question_male.append('ok sir , your passport number ?')
idnumberlist_question_male.append('get it , what is your passport number , sir ?')
idnumberlist_question_male.append('i see , please tell me your passport number , sir .')
idnumberlist_question_male.append('well sir , your passport number , please .')
idnumberlist_question_unisex = []
idnumberlist_question_unisex.append('may i have your passport number , please ?')
idnumberlist_question_unisex.append('may i have your passport number .')
idnumberlist_question_unisex.append('your passport number , please .')
idnumberlist_question_unisex.append('please tell me your passport number .')
idnumberlist_question_unisex.append('hello , i need your passport number .')
idnumberlist_question_unisex.append('hello , i need the passport number .')
idnumberlist_question_unisex.append('please tell me the passport number .')
idnumberlist_question_unisex.append('please tell me the passenger\'s passport number .')
idnumberlist_question_unisex.append('the passenger\'s passport number is ?')
idnumberlist_question_unisex.append('what is your passport number ?')
idnumberlist_question_unisex.append('we need to known your passport number .')
idnumberlist_question_unisex.append('passport number ?')
idnumberlist_question_unisex.append('passport number , please .')
idnumberlist_question_unisex.append('need your passport number , thanks .')
idnumberlist_question_unisex.append('passport number , thanks .')
idnumberlist_question_unisex.append('could you tell me the passport number ?')
idnumberlist_question_unisex.append('ok , please tell me your passport number , thanks very much .')
idnumberlist_question_unisex.append('ok , your passport number ?')
idnumberlist_question_unisex.append('get it , what is your passport number ?')
idnumberlist_question_unisex.append('i see , please tell me your passport number .')
idnumberlist_question_unisex.append('well , your passport number , please .')

idnumberlist_question_female_split = []
for ans in idnumberlist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_female_split.append(w_sent)

idnumberlist_question_male_split = []
for ans in idnumberlist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_male_split.append(w_sent)

idnumberlist_question_unisex_split = []
for ans in idnumberlist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_unisex_split.append(w_sent)

pass
