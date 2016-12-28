# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

departurelist_question_female = []
departurelist_question_female.append('what is the departure city , miss ?')
departurelist_question_female.append('miss , where do you take off ?')
departurelist_question_female.append('miss , which city are you going to take off from ?')
departurelist_question_female.append('please tell me your departure city , miss .')
departurelist_question_female.append('please tell me where do you take off , miss ?')
departurelist_question_female.append('miss , where do you go ?')
departurelist_question_female.append('miss , your departure city , please .')
departurelist_question_female.append('miss , where is the starting city of your trip ?')
departurelist_question_female.append('ok miss , please tell me where is the starting city ?')

departurelist_question_male = []
departurelist_question_male.append('what is the departure city , sir ?')
departurelist_question_male.append('sir , where do you take off ?')
departurelist_question_male.append('sir , which city are you going to take off from ?')
departurelist_question_male.append('please tell me your departure city , sir .')
departurelist_question_male.append('please tell me where do you take off , sir ?')
departurelist_question_male.append('sir , where do you go ?')
departurelist_question_male.append('sir , your departure city , please .')
departurelist_question_male.append('sir , where is the starting city of your trip ?')
departurelist_question_male.append('ok sir , please tell me where is the starting city ?')

departurelist_question_unisex = []
departurelist_question_unisex.append('what is the departure city ?')
departurelist_question_unisex.append('which airport of your departure ?')
departurelist_question_unisex.append('where do you take off ?')
departurelist_question_unisex.append('which city are you going to take off from ?')
departurelist_question_unisex.append('please tell me your departure city .')
departurelist_question_unisex.append('please tell me where do you take off ?')
departurelist_question_unisex.append('where do you go ?')
departurelist_question_unisex.append('your departure city , please .')
departurelist_question_unisex.append('where is the starting city of your trip ?')
departurelist_question_unisex.append('ok , please tell me where is the starting city ?')

departurelist_question_female_split = []
for ans in departurelist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_female_split.append(w_sent)

departurelist_question_male_split = []
for ans in departurelist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_male_split.append(w_sent)

departurelist_question_unisex_split = []
for ans in departurelist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_unisex_split.append(w_sent)

departurelist_question_female_split += departurelist_question_unisex_split
departurelist_question_male_split += departurelist_question_unisex_split
pass
