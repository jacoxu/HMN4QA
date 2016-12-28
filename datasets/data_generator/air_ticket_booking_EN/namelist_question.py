# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

namelist_question_female = []
namelist_question_female.append('hello miss , can i have your name ?')
namelist_question_female.append('miss , what is your name , please ?')
namelist_question_female.append('miss , please tell me your name .')
namelist_question_female.append('could you please tell me your name , miss .')
namelist_question_female.append('what is the user name , miss ?')
namelist_question_female.append('miss , may i have your name , please ?')
namelist_question_female.append('please let me know your name , miss .')
namelist_question_female.append('i need to know your name , miss .')
namelist_question_female.append('what should i call you , miss ?')
namelist_question_female.append('what is your full name , miss ?')
namelist_question_female.append('please tell me your full name , miss .')
namelist_question_female.append('what is your name , miss ?')
namelist_question_female.append('what\'s your name , miss ?')
namelist_question_female.append('may i know your name , miss ?')
namelist_question_female.append('what is the name of the passenger , miss ?')
namelist_question_female.append('passenger name , miss ?')
namelist_question_female.append('miss , can you please tell me your name ?')
namelist_question_female.append('miss , please tell me your name , thanks .')
namelist_question_female.append('miss , please let me know your name , thanks .')
namelist_question_female.append('miss , please tell me your name , thanks very much .')
namelist_question_female.append('your name , miss ?')
namelist_question_female.append('miss , your name , please .')
namelist_question_female.append('miss , passenger name , please .')
namelist_question_female.append('name , miss ?')

namelist_question_male = []
namelist_question_male.append('hello sir , can i have your name ?')
namelist_question_male.append('sir , what is your name , please ?')
namelist_question_male.append('sir , please tell me your name .')
namelist_question_male.append('could you please tell me your name , sir .')
namelist_question_male.append('what is the user name , sir ?')
namelist_question_male.append('sir , may i have your name , please ?')
namelist_question_male.append('please let me know your name , sir .')
namelist_question_male.append('i need to know your name , sir .')
namelist_question_male.append('what should i call you , sir ?')
namelist_question_male.append('what is your full name , sir ?')
namelist_question_male.append('please tell me your full name , sir .')
namelist_question_male.append('what is your name , sir ?')
namelist_question_male.append('what\'s your name , sir ?')
namelist_question_male.append('may i know your name , sir ?')
namelist_question_male.append('what is the name of the passenger , sir ?')
namelist_question_male.append('passenger name , sir ?')
namelist_question_male.append('sir , can you please tell me your name ?')
namelist_question_male.append('sir , please tell me your name , thanks .')
namelist_question_male.append('sir , please let me know your name , thanks .')
namelist_question_male.append('sir , please tell me your name , thanks very much .')
namelist_question_male.append('your name , sir ?')
namelist_question_male.append('sir , your name , please .')
namelist_question_male.append('sir , passenger name , please .')
namelist_question_male.append('name , sir ?')

namelist_question_unisex = []
namelist_question_unisex.append('hello , can i have your name ?')
namelist_question_unisex.append('what is your name , please ?')
namelist_question_unisex.append('please tell me your name .')
namelist_question_unisex.append('could you please tell me your name .')
namelist_question_unisex.append('what is the user name ?')
namelist_question_unisex.append('may i have your name , please ?')
namelist_question_unisex.append('please let me know your name .')
namelist_question_unisex.append('i need to know your name .')
namelist_question_unisex.append('what should i call you ?')
namelist_question_unisex.append('what is your full name ?')
namelist_question_unisex.append('please tell me your full name .')
namelist_question_unisex.append('what is your name ?')
namelist_question_unisex.append('what\'s your name ?')
namelist_question_unisex.append('may i know your name ?')
namelist_question_unisex.append('what is the name of the passenger ?')
namelist_question_unisex.append('passenger name ?')
namelist_question_unisex.append('can you please tell me your name ?')
namelist_question_unisex.append('please tell me your name , thanks .')
namelist_question_unisex.append('please let me know your name , thanks .')
namelist_question_unisex.append('please tell me your name , thanks very much .')
namelist_question_unisex.append('your name ?')
namelist_question_unisex.append('your name , please .')
namelist_question_unisex.append('passenger name , please .')
namelist_question_unisex.append('name ?')

namelist_question_female_split = []
for ans in namelist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_female_split.append(w_sent)

namelist_question_male_split = []
for ans in namelist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_male_split.append(w_sent)

namelist_question_unisex_split = []
for ans in namelist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_unisex_split.append(w_sent)

namelist_question_female_split += namelist_question_unisex_split
namelist_question_male_split += namelist_question_unisex_split
pass
