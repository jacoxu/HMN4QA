# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

roomtypelist_question_female = []
roomtypelist_question_female.append('miss , what type of room would you like ?')
roomtypelist_question_female.append('miss , which kind of room do you need ?')
roomtypelist_question_female.append('please tell me the room type you want to reserve , miss .')
roomtypelist_question_female.append('please tell me which kind of room do you need , miss ?')
roomtypelist_question_female.append('which kind of room do you want to book , miss ?')
roomtypelist_question_female.append('which kind of room , miss ?')
roomtypelist_question_female.append('miss , which type of hotel room to book ?')
roomtypelist_question_female.append('miss , tell me which type of room do you like ?')
roomtypelist_question_female.append('miss , which type of hotel room to reserve ?')
roomtypelist_question_female.append('miss , which kind of room do you want to select ?')
roomtypelist_question_female.append('which type of room , miss ?')
roomtypelist_question_female.append('ok miss , which type of room ?')
roomtypelist_question_female.append('ok miss , which type of room do you like ?')
roomtypelist_question_female.append('ok miss , please tell me which type of hotel room ?')


roomtypelist_question_male = []
roomtypelist_question_male.append('sir , what type of room would you like ?')
roomtypelist_question_male.append('sir , which kind of room do you need ?')
roomtypelist_question_male.append('please tell me the room type you want to reserve , sir .')
roomtypelist_question_male.append('please tell me which kind of room do you need , sir ?')
roomtypelist_question_male.append('which kind of room do you want to book , sir ?')
roomtypelist_question_male.append('which kind of room , sir ?')
roomtypelist_question_male.append('sir , which type of hotel room to book ?')
roomtypelist_question_male.append('sir , tell me which type of room do you like ?')
roomtypelist_question_male.append('sir , which type of hotel room to reserve ?')
roomtypelist_question_male.append('sir , which kind of room do you want to select ?')
roomtypelist_question_male.append('which type of room , sir ?')
roomtypelist_question_male.append('ok sir , which type of room ?')
roomtypelist_question_male.append('ok sir , which type of room do you like ?')
roomtypelist_question_male.append('ok sir , please tell me which type of hotel room ?')

roomtypelist_question_unisex = []
roomtypelist_question_unisex.append('what type of room would you like ?')
roomtypelist_question_unisex.append('which kind of room do you need ?')
roomtypelist_question_unisex.append('please tell me the room type you want to reserve .')
roomtypelist_question_unisex.append('please tell me which kind of room do you need ?')
roomtypelist_question_unisex.append('which kind of room do you want to book ?')
roomtypelist_question_unisex.append('which kind of room ?')
roomtypelist_question_unisex.append('which type of hotel room to book ?')
roomtypelist_question_unisex.append('tell me which type of room do you like ?')
roomtypelist_question_unisex.append('which type of hotel room to reserve ?')
roomtypelist_question_unisex.append('which kind of room do you want to select ?')
roomtypelist_question_unisex.append('which type of room ?')
roomtypelist_question_unisex.append('ok , which type of room ?')
roomtypelist_question_unisex.append('ok , which type of room do you like ?')
roomtypelist_question_unisex.append('ok , please tell me which type of hotel room ?')

roomtpyelist_question_female_split = []
for ans in roomtypelist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtpyelist_question_female_split.append(w_sent)

roomtypelist_question_male_split = []
for ans in roomtypelist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtypelist_question_male_split.append(w_sent)

roomtypelist_question_unisex_split = []
for ans in roomtypelist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtypelist_question_unisex_split.append(w_sent)

roomtpyelist_question_female_split += roomtypelist_question_unisex_split
roomtypelist_question_male_split += roomtypelist_question_unisex_split
pass
