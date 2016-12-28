# -*- coding: utf8 -*-
__author__ = 'shin'

destinationlist_question_female = []
destinationlist_question_female.append('miss , what is the destination city ?')
destinationlist_question_female.append('which airport of your destination , miss ?')
destinationlist_question_female.append('may i ask where is your destination city , miss ?')
destinationlist_question_female.append('to which city , miss ?')
destinationlist_question_female.append('miss , which city are you going to travel to ?')
destinationlist_question_female.append('please tell me your destination city , miss .')
destinationlist_question_female.append('miss , please tell me which city do you go to ?')
destinationlist_question_female.append('miss , where do you go ?')
destinationlist_question_female.append('miss , your destination city , please .')
destinationlist_question_female.append('ok miss , please tell me where is the destination city ?')
destinationlist_question_female.append('where are you traveling to , miss ?')
destinationlist_question_female.append('what is your destination , miss ?')
destinationlist_question_female.append('miss , what city are you flying to ?')
destinationlist_question_female.append('miss , where are you flying to ?')

destinationlist_question_male = []
destinationlist_question_male.append('sir , what is the destination city ?')
destinationlist_question_male.append('which airport of your destination , sir ?')
destinationlist_question_male.append('may i ask where is your destination city , sir ?')
destinationlist_question_male.append('to which city , sir ?')
destinationlist_question_male.append('sir , which city are you going to travel to ?')
destinationlist_question_male.append('please tell me your destination city , sir .')
destinationlist_question_male.append('sir , please tell me which city do you go to ?')
destinationlist_question_male.append('sir , where do you go ?')
destinationlist_question_male.append('sir , your destination city , please .')
destinationlist_question_male.append('ok sir , please tell me where is the destination city ?')
destinationlist_question_male.append('where are you traveling to , sir ?')
destinationlist_question_male.append('what is your destination , sir ?')
destinationlist_question_male.append('what city are you flying to , sir ?')
destinationlist_question_male.append('sir , where are you flying to ?')

destinationlist_question_unisex = []
destinationlist_question_unisex.append('what is the destination city ?')
destinationlist_question_unisex.append('which airport of your destination ?')
destinationlist_question_unisex.append('may i ask where is your destination city ?')
destinationlist_question_unisex.append('to which city ?')
destinationlist_question_unisex.append('which city are you going to travel to ?')
destinationlist_question_unisex.append('please tell me your destination city .')
destinationlist_question_unisex.append('please tell me which city do you go to ?')
destinationlist_question_unisex.append('where do you go ?')
destinationlist_question_unisex.append('your destination city , please .')
destinationlist_question_unisex.append('ok , please tell me where is the destination city ?')
destinationlist_question_unisex.append('where are you traveling to ?')
destinationlist_question_unisex.append('what is your destination ?')
destinationlist_question_unisex.append('what\'s your destination ?')
destinationlist_question_unisex.append('what city are you flying to ?')
destinationlist_question_unisex.append('where are you flying to ?')

destinationlist_question_female_split = []
for ans in destinationlist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_female_split.append(w_sent)

destinationlist_question_male_split = []
for ans in destinationlist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_male_split.append(w_sent)

destinationlist_question_unisex_split = []
for ans in destinationlist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_unisex_split.append(w_sent)

destinationlist_question_female_split += destinationlist_question_unisex_split
destinationlist_question_male_split += destinationlist_question_unisex_split
pass
