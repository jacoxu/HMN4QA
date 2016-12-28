# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

timelist_question_female = []
timelist_question_female.append('miss , what date will you check in on ?')
timelist_question_female.append('miss , what is your check in date ?')
timelist_question_female.append('miss , what date would you like me to book this hotel for ?')
timelist_question_female.append('miss , when do you want to check in ?')
timelist_question_female.append('please tell me when do you want to check in , miss ?')
timelist_question_female.append('miss , when will you check in ?')
timelist_question_female.append('when will you arrival , miss ?')
timelist_question_female.append('miss , when would you like to arrival the hotel ?')
timelist_question_female.append('when would you like to arrival , miss ?')
timelist_question_female.append('when are you arriving , miss ?')
timelist_question_female.append('ok miss , what is the date ?')
timelist_question_female.append('ok miss , what is the time ?')
timelist_question_female.append('ok miss , please tell me your arrival time .')
timelist_question_female.append('miss , the arrival time is ?')
timelist_question_female.append('miss , tell me your arrival time , thanks .')

timelist_question_male = []
timelist_question_male.append('sir , what date will you check in on ?')
timelist_question_male.append('sir , what is your check in date ?')
timelist_question_male.append('sir , what date would you like me to book this hotel for ?')
timelist_question_male.append('sir , when do you want to check in ?')
timelist_question_male.append('please tell me when do you want to check in , sir ?')
timelist_question_male.append('sir , when will you check in ?')
timelist_question_male.append('when will you arrival , sir ?')
timelist_question_male.append('sir , when would you like to arrival the hotel ?')
timelist_question_male.append('when would you like to arrival , sir ?')
timelist_question_male.append('when are you arriving , sir ?')
timelist_question_male.append('ok sir , what is the date ?')
timelist_question_male.append('ok sir , what is the time ?')
timelist_question_male.append('ok sir , please tell me your arrival time .')
timelist_question_male.append('sir , the arrival time is ?')
timelist_question_male.append('sir , tell me your arrival time , thanks .')

timelist_question_unisex = []
timelist_question_unisex.append('what date will you check in on ?')
timelist_question_unisex.append('what is your check in date ?')
timelist_question_unisex.append('what date would you like me to book this hotel for ?')
timelist_question_unisex.append('when do you want to check in ?')
timelist_question_unisex.append('please tell me when do you want to check in ?')
timelist_question_unisex.append('when will you check in ?')
timelist_question_unisex.append('when will you arrival ?')
timelist_question_unisex.append('when would you like to arrival the hotel ?')
timelist_question_unisex.append('when would you like to arrival ?')
timelist_question_unisex.append('when are you arriving ?')
timelist_question_unisex.append('ok , what is the date ?')
timelist_question_unisex.append('ok , what is the time ?')
timelist_question_unisex.append('ok , please tell me your arrival time .')
timelist_question_unisex.append('the arrival time is ?')
timelist_question_unisex.append('tell me your arrival time , thanks .')

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
