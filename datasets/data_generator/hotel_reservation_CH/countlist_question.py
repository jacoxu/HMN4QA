# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

countlist_question_female = []
countlist_question_female.append('小姐，您要订几个房间？')
countlist_question_female.append('女士，您需要几个房间？')
countlist_question_female.append('您要多少房间，女士？')
countlist_question_female.append('女士，您订几间？')
countlist_question_female.append('小姐，您要订多少间？')
countlist_question_female.append('女士，您想预订几间？')
countlist_question_female.append('小姐，您想要订多少间？')
countlist_question_female.append('小姐，您订几间房？')
countlist_question_female.append('女士，您需要预订多少间房？')
countlist_question_female.append('小姐，要订几间房间？')
countlist_question_female.append('需要几间？小姐')
countlist_question_female.append('需要多少间？女士')
countlist_question_female.append('需要几间房？小姐')
countlist_question_female.append('需要多少间房？女士')
countlist_question_female.append('需要房间的数量是多少？小姐')
countlist_question_female.append('小姐，您预订的数量？')
countlist_question_female.append('小姐，房间数量？')
countlist_question_female.append('女士，您预订的数量是？')
countlist_question_female.append('小姐，房间数目？')
countlist_question_female.append('小姐，订几间？')
countlist_question_female.append('女士，订几个？')
countlist_question_female.append('小姐，预订数量？')
countlist_question_female.append('小姐，您要订几间？谢谢。')
countlist_question_female.append('好的小姐，请告诉我您要订几间？')
countlist_question_female.append('ok，没问题小姐，订几间？')
countlist_question_female.append('女士，您需要几间房间？')
countlist_question_female.append('小姐，请告诉我您需要多少间房间呢？')
countlist_question_female.append('女士，您想要几间房间呢？')
countlist_question_female.append('女士，您需要多少？谢谢。')
countlist_question_female.append('麻烦您说下订几间，小姐。')
countlist_question_female.append('知道了小姐，订几间呀？')
countlist_question_female.append('明白了小姐，麻烦说下订几间？')
countlist_question_female.append('好的，没问题小姐，想要多少间呀？')
countlist_question_female.append('小姐，订几间房呀？')
countlist_question_female.append('小姐，您要订多少间呢，谢谢。')

countlist_question_male = []
countlist_question_male.append('先生，您要订几个房间？')
countlist_question_male.append('先生，您需要几个房间？')
countlist_question_male.append('您要多少房间，先生？')
countlist_question_male.append('先生，您订几间？')
countlist_question_male.append('先生，您要订多少间？')
countlist_question_male.append('先生，您想预订几间？')
countlist_question_male.append('先生，您想要订多少间？')
countlist_question_male.append('先生，您订几间房？')
countlist_question_male.append('先生，您需要预订多少间房？')
countlist_question_male.append('先生，要订几间房间？')
countlist_question_male.append('需要几间？先生')
countlist_question_male.append('需要多少间？先生')
countlist_question_male.append('需要几间房？先生')
countlist_question_male.append('需要多少间房？先生')
countlist_question_male.append('需要房间的数量是多少？先生')
countlist_question_male.append('先生，您预订的数量？')
countlist_question_male.append('先生，房间数量？')
countlist_question_male.append('先生，您预订的数量是？')
countlist_question_male.append('先生，房间数目？')
countlist_question_male.append('先生，订几间？')
countlist_question_male.append('先生，订几个？')
countlist_question_male.append('先生，预订数量？')
countlist_question_male.append('先生，您要订几间？谢谢。')
countlist_question_male.append('好的先生，请告诉我您要订几间？')
countlist_question_male.append('ok，没问题先生，订几间？')
countlist_question_male.append('先生，您需要几间房间？')
countlist_question_male.append('先生，请告诉我您需要多少间房间呢？')
countlist_question_male.append('先生，您想要几间房间呢？')
countlist_question_male.append('先生，您需要多少？谢谢。')
countlist_question_male.append('麻烦您说下订几间，先生。')
countlist_question_male.append('知道了先生，订几间呀？')
countlist_question_male.append('明白了先生，麻烦说下订几间？')
countlist_question_male.append('好的，没问题先生，想要多少间呀？')
countlist_question_male.append('先生，订几间房呀？')
countlist_question_male.append('先生，您要订多少间呢，谢谢。')

countlist_question_unisex = []
countlist_question_unisex.append('您要订几个房间？')
countlist_question_unisex.append('您需要几个房间？')
countlist_question_unisex.append('您要多少房间？')
countlist_question_unisex.append('您订几间？')
countlist_question_unisex.append('您要订多少间？')
countlist_question_unisex.append('您想预订几间？')
countlist_question_unisex.append('您想要订多少间？')
countlist_question_unisex.append('您订几间房？')
countlist_question_unisex.append('您需要预订多少间房？')
countlist_question_unisex.append('要订几间房间？')
countlist_question_unisex.append('需要几间？')
countlist_question_unisex.append('需要多少间？')
countlist_question_unisex.append('需要几间房？')
countlist_question_unisex.append('需要多少间房？')
countlist_question_unisex.append('需要房间的数量是多少？')
countlist_question_unisex.append('您预订的数量？')
countlist_question_unisex.append('房间数量？')
countlist_question_unisex.append('您预订的数量是？')
countlist_question_unisex.append('房间数目？')
countlist_question_unisex.append('订几间？')
countlist_question_unisex.append('订几个？')
countlist_question_unisex.append('预订数量？')
countlist_question_unisex.append('您要订几间？谢谢。')
countlist_question_unisex.append('好的，请告诉我您要订几间？')
countlist_question_unisex.append('ok，没问题，订几间？')
countlist_question_unisex.append('您需要几间房间？')
countlist_question_unisex.append('请告诉我您需要多少间房间呢？')
countlist_question_unisex.append('您想要几间房间呢？')
countlist_question_unisex.append('您需要多少？谢谢。')
countlist_question_unisex.append('麻烦您说下订几间。')
countlist_question_unisex.append('知道了，订几间呀？')
countlist_question_unisex.append('明白了，麻烦说下订几间？')
countlist_question_unisex.append('好的，没问题，想要多少间呀？')
countlist_question_unisex.append('订几间房呀？')
countlist_question_unisex.append('您要订多少间呢，谢谢。')

countlist_question_female_split = []
for ans in countlist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_female_split.append(w_sent)

countlist_question_male_split = []
for ans in countlist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_male_split.append(w_sent)

countlist_question_unisex_split = []
for ans in countlist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    countlist_question_unisex_split.append(w_sent)

countlist_question_female_split += countlist_question_unisex_split
countlist_question_male_split += countlist_question_unisex_split
pass
