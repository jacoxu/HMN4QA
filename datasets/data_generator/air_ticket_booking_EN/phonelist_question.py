# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

phonelist_question_female = []
phonelist_question_female.append('miss , may i have your phone number ?')
phonelist_question_female.append('may i have your cell phone number , miss ?')
phonelist_question_female.append('please tell me your phone number , miss .')
phonelist_question_female.append('hello miss , i need your phone number .')
phonelist_question_female.append('please tell me the passenger\'s phone number , miss .')
phonelist_question_female.append('miss , the passenger\'s phone number is ?')
phonelist_question_female.append('what is your phone number , miss ?')
phonelist_question_female.append('can you please tell me your telephone number , miss ?')
phonelist_question_female.append('what\'s your phone number , miss ?')
phonelist_question_female.append('we need to know your phone number , miss .')
phonelist_question_female.append('the phone number , miss ?')
phonelist_question_female.append('your contact number , miss ?')
phonelist_question_female.append('please tell me your contact number , miss .')
phonelist_question_female.append('miss , contact number ? thanks .')
phonelist_question_female.append('miss , may i have your phone number , thanks .')
phonelist_question_female.append('ok miss , please tell me your phone number , thanks very much .')
phonelist_question_female.append('get it miss , your phone number ?')
phonelist_question_female.append('get it miss , please tell me your phone number .')
phonelist_question_female.append('hmm miss , the phone number ? thanks .')
phonelist_question_female.append('please tell me your contact information miss .')
phonelist_question_female.append('hello miss , we need your contact information .')

phonelist_question_male = []
phonelist_question_male.append('sir , may i have your phone number ?')
phonelist_question_male.append('may i have your cell phone number , sir ?')
phonelist_question_male.append('please tell me your phone number , sir .')
phonelist_question_male.append('hello sir , i need your phone number .')
phonelist_question_male.append('please tell me the passenger\'s phone number , sir .')
phonelist_question_male.append('sir , the passenger\'s phone number is ?')
phonelist_question_male.append('what is your phone number , sir ?')
phonelist_question_male.append('can you please tell me your telephone number , sir ?')
phonelist_question_male.append('what\'s your phone number , sir ?')
phonelist_question_male.append('we need to know your phone number , sir .')
phonelist_question_male.append('the phone number , sir ?')
phonelist_question_male.append('your contact number , sir ?')
phonelist_question_male.append('please tell me your contact number , sir .')
phonelist_question_male.append('sir , contact number ? thanks .')
phonelist_question_male.append('sir , may i have your phone number , thanks .')
phonelist_question_male.append('ok sir , please tell me your phone number , thanks very much .')
phonelist_question_male.append('get it sir , your phone number ?')
phonelist_question_male.append('get it sir , please tell me your phone number .')
phonelist_question_male.append('hmm sir , the phone number ? thanks .')
phonelist_question_male.append('please tell me your contact information sir .')
phonelist_question_male.append('hello sir , we need your contact information .')

phonelist_question_unisex = []
phonelist_question_unisex.append('may i have your phone number ?')
phonelist_question_unisex.append('may i have your cell phone number ?')
phonelist_question_unisex.append('please tell me your phone number .')
phonelist_question_unisex.append('hello , i need your phone number .')
phonelist_question_unisex.append('please tell me the passenger\'s phone number .')
phonelist_question_unisex.append('the passenger\'s phone number is ?')
phonelist_question_unisex.append('what is your phone number ?')
phonelist_question_unisex.append('can you please tell me your telephone number ?')
phonelist_question_unisex.append('what\'s your phone number ?')
phonelist_question_unisex.append('we need to know your phone number .')
phonelist_question_unisex.append('the phone number ?')
phonelist_question_unisex.append('your contact number ?')
phonelist_question_unisex.append('please tell me your contact number .')
phonelist_question_unisex.append('contact number ? thanks .')
phonelist_question_unisex.append('may i have your phone number , thanks .')
phonelist_question_unisex.append('ok , please tell me your phone number , thanks very much .')
phonelist_question_unisex.append('get it , your phone number ?')
phonelist_question_unisex.append('get it , please tell me your phone number .')
phonelist_question_unisex.append('hmm , the phone number ? thanks .')
phonelist_question_unisex.append('please tell me your contact information .')
phonelist_question_unisex.append('hello , we need your contact information .')

phonelist_question_female_split = []
for ans in phonelist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_female_split.append(w_sent)

phonelist_question_male_split = []
for ans in phonelist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_male_split.append(w_sent)

phonelist_question_unisex_split = []
for ans in phonelist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_unisex_split.append(w_sent)

phonelist_question_female_split += phonelist_question_unisex_split
phonelist_question_male_split += phonelist_question_unisex_split

pass
