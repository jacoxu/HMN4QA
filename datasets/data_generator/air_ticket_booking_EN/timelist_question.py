# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

timelist_question_female = []
timelist_question_female.append('what date will you be traveling , miss ?')
timelist_question_female.append('what is your travel date , miss ?')
timelist_question_female.append('miss , what date would you like me to book this plane ticket for ?')
timelist_question_female.append('miss , when do you want to go ?')
timelist_question_female.append('please tell me when do you want to go , miss ?')
timelist_question_female.append('miss , when will you be leaving ?')
timelist_question_female.append('miss , when do you want to travel ?')
timelist_question_female.append('when would you like to book the ticket , miss ?')
timelist_question_female.append('miss , when would you like to buy ?')
timelist_question_female.append('miss , when are you leaving ?')
timelist_question_female.append('miss , when are you going ?')
timelist_question_female.append('ok miss , what is the date ?')
timelist_question_female.append('ok miss , what is the time ?')
timelist_question_female.append('ok miss , please tell me your travel time .')
timelist_question_female.append('miss , the travel time is ?')
timelist_question_female.append('miss , tell me your travel time , thanks .')

timelist_question_male = []
timelist_question_male.append('what date will you be traveling , sir ?')
timelist_question_male.append('what is your travel date , sir ?')
timelist_question_male.append('sir , what date would you like me to book this plane ticket for ?')
timelist_question_male.append('sir , when do you want to go ?')
timelist_question_male.append('please tell me when do you want to go , sir ?')
timelist_question_male.append('sir , when will you be leaving ?')
timelist_question_male.append('sir , when do you want to travel ?')
timelist_question_male.append('when would you like to book the ticket , sir ?')
timelist_question_male.append('sir , when would you like to buy ?')
timelist_question_male.append('sir , when are you leaving ?')
timelist_question_male.append('sir , when are you going ?')
timelist_question_male.append('ok sir , what is the date ?')
timelist_question_male.append('ok sir , what is the time ?')
timelist_question_male.append('ok sir , please tell me your travel time .')
timelist_question_male.append('sir , the travel time is ?')
timelist_question_male.append('sir , tell me your travel time , thanks .')

timelist_question_unisex = []
timelist_question_unisex.append('what date will you be traveling on ?')
timelist_question_unisex.append('what is your travel date ?')
timelist_question_unisex.append('what date would you like me to book this plane ticket for ?')
timelist_question_unisex.append('when do you want to go ?')
timelist_question_unisex.append('please tell me when do you want to go ?')
timelist_question_unisex.append('when will you be leaving ?')
timelist_question_unisex.append('when do you want to travel ?')
timelist_question_unisex.append('when would you like to book the ticket ?')
timelist_question_unisex.append('when would you like to buy ?')
timelist_question_unisex.append('when are you leaving ?')
timelist_question_unisex.append('when are you going ?')
timelist_question_unisex.append('ok , what is the date ?')
timelist_question_unisex.append('ok , what is the time ?')
timelist_question_unisex.append('ok , please tell me your travel time .')
timelist_question_unisex.append('the travel time is ?')
timelist_question_unisex.append('tell me your travel time , thanks .')

timelist_question_female_split = []
for ans in timelist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_female_split.append(w_sent)

timelist_question_male_split = []
for ans in timelist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_male_split.append(w_sent)

timelist_question_unisex_split = []
for ans in timelist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    timelist_question_unisex_split.append(w_sent)

timelist_question_female_split += timelist_question_unisex_split
timelist_question_male_split += timelist_question_unisex_split
pass
