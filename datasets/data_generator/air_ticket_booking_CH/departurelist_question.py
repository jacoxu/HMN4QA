# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

departurelist_question_female = []
departurelist_question_female.append('请问女士您从哪里起飞？')
departurelist_question_female.append('请问小姐您从哪里出行？')
departurelist_question_female.append('请问女士您从哪个城市出行？')
departurelist_question_female.append('小姐，请告诉我您的起飞城市。')
departurelist_question_female.append('请女士告诉我，您从哪个城市出行？')
departurelist_question_female.append('小姐，您从哪里走？')
departurelist_question_female.append('女士，您从哪里出发呢？')
departurelist_question_female.append('小姐，您从哪里起飞？')
departurelist_question_female.append('说下小姐您的出发地？')
departurelist_question_female.append('小姐，您旅行的起点是哪里？')
departurelist_question_female.append('小姐，您从哪座城市出发？')
departurelist_question_female.append('小姐，从哪走？')
departurelist_question_female.append('小姐，在哪里起飞？')
departurelist_question_female.append('您要买从哪里出发的机票，女士？')
departurelist_question_female.append('好的，麻烦女士说一下起点是哪里？')

departurelist_question_male = []
departurelist_question_male.append('请问先生您从哪里起飞？')
departurelist_question_male.append('请问先生您从哪里出行？')
departurelist_question_male.append('请问先生您从哪个城市出行？')
departurelist_question_male.append('先生，请告诉我您的起飞城市。')
departurelist_question_male.append('请先生告诉我，您从哪个城市出行？')
departurelist_question_male.append('先生，您从哪里走？')
departurelist_question_male.append('先生，您从哪里出发呢？')
departurelist_question_male.append('先生，您从哪里起飞？')
departurelist_question_male.append('说下先生您的出发地？')
departurelist_question_male.append('先生，您旅行的起点是哪里？')
departurelist_question_male.append('先生，您从哪座城市出发？')
departurelist_question_male.append('先生，从哪走？')
departurelist_question_male.append('先生，在哪里起飞？')
departurelist_question_male.append('您要买从哪里出发的机票，先生？')
departurelist_question_male.append('好的，麻烦先生说一下起点是哪里？')

departurelist_question_unisex = []
departurelist_question_unisex.append('请问您从哪里起飞？')
departurelist_question_unisex.append('请问您从哪里出行？')
departurelist_question_unisex.append('请问您从哪个城市出行？')
departurelist_question_unisex.append('请告诉我您的起飞城市。')
departurelist_question_unisex.append('请您告诉我，您从哪个城市出行？')
departurelist_question_unisex.append('您从哪里走？')
departurelist_question_unisex.append('您从哪里出发呢？')
departurelist_question_unisex.append('您从哪里起飞？')
departurelist_question_unisex.append('说下您的出发地？')
departurelist_question_unisex.append('您旅行的起点是哪里？')
departurelist_question_unisex.append('您从哪座城市出发？')
departurelist_question_unisex.append('从哪走？')
departurelist_question_unisex.append('在哪里起飞？')
departurelist_question_unisex.append('您要买从哪里出发的机票？')
departurelist_question_unisex.append('好的，麻烦说一下起点是哪里？')

departurelist_question_female_split = []
for ans in departurelist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_female_split.append(w_sent)

departurelist_question_male_split = []
for ans in departurelist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_male_split.append(w_sent)

departurelist_question_unisex_split = []
for ans in departurelist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    departurelist_question_unisex_split.append(w_sent)

departurelist_question_female_split += departurelist_question_unisex_split
departurelist_question_male_split += departurelist_question_unisex_split
pass
