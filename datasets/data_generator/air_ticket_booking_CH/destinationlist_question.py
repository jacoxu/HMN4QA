# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

destinationlist_question_female = []
destinationlist_question_female.append('请问女士您的目的地是哪里？')
destinationlist_question_female.append('小姐，请问您要预定的目的地是？')
destinationlist_question_female.append('请问小姐您要预定飞往哪个城市的机票？')
destinationlist_question_female.append('请问女士您此次出行的目的地是？')
destinationlist_question_female.append('请问小姐您此次前往哪个城市？')
destinationlist_question_female.append('女士，您要去什么地方？')
destinationlist_question_female.append('小姐，您要飞往什么地方？')
destinationlist_question_female.append('小姐，您要飞往哪座城市？')
destinationlist_question_female.append('小姐，您想订去哪里的飞机票？')
destinationlist_question_female.append('去哪？女士')
destinationlist_question_female.append('去哪儿？小姐')
destinationlist_question_female.append('往哪里去？女士')
destinationlist_question_female.append('去到哪里？小姐')
destinationlist_question_female.append('小姐，您机票的目的地是哪里？')
destinationlist_question_female.append('女士，您的目的地？')
destinationlist_question_female.append('小姐，您要订飞往那里的票？')
destinationlist_question_female.append('请告诉我您旅行的目的地，女士。')
destinationlist_question_female.append('女士，您告诉我您的目的地。')
destinationlist_question_female.append('没问题，麻烦说下目的地，女士。')

destinationlist_question_male = []
destinationlist_question_male.append('请问先生您的目的地是哪里？')
destinationlist_question_male.append('先生，请问您要预定的目的地是？')
destinationlist_question_male.append('请问先生您要预定飞往哪个城市的机票？')
destinationlist_question_male.append('请问先生您此次出行的目的地是？')
destinationlist_question_male.append('请问先生您此次前往哪个城市？')
destinationlist_question_male.append('先生，您要去什么地方？')
destinationlist_question_male.append('先生，您要飞往什么地方？')
destinationlist_question_male.append('先生，您要飞往哪座城市？')
destinationlist_question_male.append('先生，您想订去哪里的飞机票？')
destinationlist_question_male.append('去哪？先生')
destinationlist_question_male.append('去哪儿？先生')
destinationlist_question_male.append('往哪里去？先生')
destinationlist_question_male.append('去到哪里？先生')
destinationlist_question_male.append('先生，您机票的目的地是哪里？')
destinationlist_question_male.append('先生，您的目的地？')
destinationlist_question_male.append('先生，您要订飞往那里的票？')
destinationlist_question_male.append('请告诉我您旅行的目的地，先生。')
destinationlist_question_male.append('先生，您告诉我您的目的地。')
destinationlist_question_male.append('没问题，麻烦说下目的地，先生。')

destinationlist_question_unisex = []
destinationlist_question_unisex.append('请问您的目的地是哪里？')
destinationlist_question_unisex.append('请问您要预定的目的地是？')
destinationlist_question_unisex.append('请问您要预定飞往哪个城市的机票？')
destinationlist_question_unisex.append('请问您此次出行的目的地是？')
destinationlist_question_unisex.append('请问您此次前往哪个城市？')
destinationlist_question_unisex.append('您要去什么地方？')
destinationlist_question_unisex.append('您要飞往什么地方？')
destinationlist_question_unisex.append('您要飞往哪座城市？')
destinationlist_question_unisex.append('您想订去哪里的飞机票？')
destinationlist_question_unisex.append('去哪？')
destinationlist_question_unisex.append('去哪儿？')
destinationlist_question_unisex.append('往哪里去？')
destinationlist_question_unisex.append('去到哪里？')
destinationlist_question_unisex.append('您机票的目的地是哪里？')
destinationlist_question_unisex.append('目的地？')
destinationlist_question_unisex.append('终点是？')
destinationlist_question_unisex.append('您的目的地？')
destinationlist_question_unisex.append('您要订飞往那里的票？')
destinationlist_question_unisex.append('去哪里的票？')
destinationlist_question_unisex.append('请告诉我您旅行的目的地。')
destinationlist_question_unisex.append('您告诉我您的目的地。')
destinationlist_question_unisex.append('没问题，麻烦说下目的地。')

destinationlist_question_female_split = []
for ans in destinationlist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_female_split.append(w_sent)

destinationlist_question_male_split = []
for ans in destinationlist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_male_split.append(w_sent)

destinationlist_question_unisex_split = []
for ans in destinationlist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    destinationlist_question_unisex_split.append(w_sent)

destinationlist_question_female_split += destinationlist_question_unisex_split
destinationlist_question_male_split += destinationlist_question_unisex_split
pass
