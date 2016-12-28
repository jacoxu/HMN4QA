# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

countlist_question_female = []
countlist_question_female.append('how many rooms , miss ?')
countlist_question_female.append('miss , how many rooms do you want ?')
countlist_question_female.append('miss , how many rooms you need ?')
countlist_question_female.append('miss , how many rooms do you want to book ?')
countlist_question_female.append('how many rooms do you want to reserve , miss ?')
countlist_question_female.append('how many hotel rooms do you want , miss ?')
countlist_question_female.append('how many hotel rooms do you want to reserve , miss ?')
countlist_question_female.append('what\'s the number of rooms , miss ?')
countlist_question_female.append('the number of rooms , miss ?')
countlist_question_female.append('miss , the number of rooms please ?')
countlist_question_female.append('miss , what is the number of rooms ? thanks .')
countlist_question_female.append('miss , the number of rooms ? thanks .')
countlist_question_female.append('ok miss , how many rooms ?')
countlist_question_female.append('ok miss , how many rooms do you want ?')
countlist_question_female.append('miss , please tell me the number of rooms .')
countlist_question_female.append('get it miss , please tell me how many rooms .')
countlist_question_female.append('hmm miss , the number of rooms please .')

countlist_question_male = []
countlist_question_male.append('how many rooms , sir ?')
countlist_question_male.append('sir , how many rooms do you want ?')
countlist_question_male.append('sir , how many rooms you need ?')
countlist_question_male.append('sir , how many rooms do you want to book ?')
countlist_question_male.append('how many rooms do you want to reserve , sir ?')
countlist_question_male.append('how many hotel rooms do you want , sir ?')
countlist_question_male.append('how many hotel rooms do you want to reserve , sir ?')
countlist_question_male.append('what\'s the number of rooms , sir ?')
countlist_question_male.append('the number of rooms , sir ?')
countlist_question_male.append('sir , the number of rooms please ?')
countlist_question_male.append('sir , what is the number of rooms ? thanks .')
countlist_question_male.append('sir , the number of rooms ? thanks .')
countlist_question_male.append('ok sir , how many rooms ?')
countlist_question_male.append('ok sir , how many rooms do you want ?')
countlist_question_male.append('sir , please tell me the number of rooms .')
countlist_question_male.append('get it sir , please tell me how many rooms .')
countlist_question_male.append('hmm sir , the number of rooms please .')

countlist_question_unisex = []
countlist_question_unisex.append('how many rooms ?')
countlist_question_unisex.append('how many rooms do you want ?')
countlist_question_unisex.append('how many rooms you need ?')
countlist_question_unisex.append('how many rooms do you want to book ?')
countlist_question_unisex.append('how many rooms do you want to reserve ?')
countlist_question_unisex.append('how many hotel rooms do you want ?')
countlist_question_unisex.append('how many hotel rooms do you want to reserve ?')
countlist_question_unisex.append('what\'s the number of rooms ?')
countlist_question_unisex.append('the number of rooms ?')
countlist_question_unisex.append('the number of rooms please ?')
countlist_question_unisex.append('what is the number of rooms ? thanks .')
countlist_question_unisex.append('the number of rooms ? thanks .')
countlist_question_unisex.append('ok , how many rooms ?')
countlist_question_unisex.append('ok , how many rooms do you want ?')
countlist_question_unisex.append('please tell me the number of rooms .')
countlist_question_unisex.append('get it , please tell me how many rooms .')
countlist_question_unisex.append('hmm , the number of rooms please .')

countlist_question_female_split = []
for ans in countlist_question_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_female_split.append(w_sent)

countlist_question_male_split = []
for ans in countlist_question_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_male_split.append(w_sent)

countlist_question_unisex_split = []
for ans in countlist_question_unisex:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_unisex_split.append(w_sent)

countlist_question_female_split += countlist_question_unisex_split
countlist_question_male_split += countlist_question_unisex_split
pass
