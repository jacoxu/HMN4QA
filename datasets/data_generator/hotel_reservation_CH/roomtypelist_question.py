# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'
import jieba

roomtypelist_question_female = []
roomtypelist_question_female.append('小姐，请问要什么样的房间？')
roomtypelist_question_female.append('请问女士您需要什么类型的房间？')
roomtypelist_question_female.append('请小姐告诉我您要预订的房间类型')
roomtypelist_question_female.append('请女士告诉我，您要订什么房间？')
roomtypelist_question_female.append('小姐，您订什么房间？')
roomtypelist_question_female.append('小姐，您订什么类型房间？')
roomtypelist_question_female.append('女士，您需要什么房间？')
roomtypelist_question_female.append('女士，说下您的房间类型？')
roomtypelist_question_female.append('小姐，您要预订什么房间类型？')
roomtypelist_question_female.append('小姐，您想选择什么类型的房间？')
roomtypelist_question_female.append('小姐，什么类型房间？')
roomtypelist_question_female.append('小姐，您想预订什么样的房间啊？')
roomtypelist_question_female.append('女士，您要预订什么房？')
roomtypelist_question_female.append('好的小姐，麻烦说一下房间类型？')


roomtypelist_question_male = []
roomtypelist_question_male.append('先生，请问要什么样的房间？')
roomtypelist_question_male.append('请问先生您需要什么类型的房间？')
roomtypelist_question_male.append('请先生告诉我您要预订的房间类型')
roomtypelist_question_male.append('请先生告诉我，您要订什么房间？')
roomtypelist_question_male.append('先生，您订什么房间？')
roomtypelist_question_male.append('先生，您订什么类型房间？')
roomtypelist_question_male.append('先生，您需要什么房间？')
roomtypelist_question_male.append('先生，说下您的房间类型？')
roomtypelist_question_male.append('先生，您要预订什么房间类型？')
roomtypelist_question_male.append('先生，您想选择什么类型的房间？')
roomtypelist_question_male.append('先生，什么类型房间？')
roomtypelist_question_male.append('先生，您想预订什么样的房间啊？')
roomtypelist_question_male.append('先生，您要预订什么房？')
roomtypelist_question_male.append('好的先生，麻烦说一下房间类型？')

roomtypelist_question_unisex = []
roomtypelist_question_unisex.append('请问要什么样的房间？')
roomtypelist_question_unisex.append('请问您需要什么类型的房间？')
roomtypelist_question_unisex.append('请告诉我您要预订的房间类型')
roomtypelist_question_unisex.append('请您告诉我，您要订什么房间？')
roomtypelist_question_unisex.append('您订什么房间？')
roomtypelist_question_unisex.append('您订什么类型房间？')
roomtypelist_question_unisex.append('您需要什么房间？')
roomtypelist_question_unisex.append('说下您的房间类型？')
roomtypelist_question_unisex.append('您要预订什么房间类型？')
roomtypelist_question_unisex.append('您想选择什么类型的房间？')
roomtypelist_question_unisex.append('什么类型房间？')
roomtypelist_question_unisex.append('您想预订什么样的房间啊？')
roomtypelist_question_unisex.append('您要预订什么房？')
roomtypelist_question_unisex.append('好的，麻烦说一下房间类型？')

roomtpyelist_question_female_split = []
for ans in roomtypelist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtpyelist_question_female_split.append(w_sent)

roomtypelist_question_male_split = []
for ans in roomtypelist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtypelist_question_male_split.append(w_sent)

roomtypelist_question_unisex_split = []
for ans in roomtypelist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    roomtypelist_question_unisex_split.append(w_sent)

roomtpyelist_question_female_split += roomtypelist_question_unisex_split
roomtypelist_question_male_split += roomtypelist_question_unisex_split
pass
