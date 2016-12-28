# -*- coding: utf8 -*-
import jieba
__author__ = 'shin & jacoxu'

namelist_question_female = []
namelist_question_female.append('请问小姐怎么称呼？')
namelist_question_female.append('请问小姐的姓名是？')
namelist_question_female.append('请女士告诉我您的名字。')
namelist_question_female.append('请问女士您的名字是？')
namelist_question_female.append('请输入女士您的全名。')
namelist_question_female.append('您叫什么名字啊，女士。')
namelist_question_female.append('请告知您的名字，女士。')
namelist_question_female.append('请问女士尊姓大名？')
namelist_question_female.append('麻烦小姐说一下您的姓名可以吗？')
namelist_question_female.append('麻烦说下您的名字？谢谢女士。')
namelist_question_female.append('您好，请问女士您的姓名是？')
namelist_question_female.append('请问女士怎么称呼？')
namelist_question_female.append('小姐您怎么称呼？')
namelist_question_female.append('小姐您叫什么名字？')
namelist_question_female.append('小姐，您的名字？')
namelist_question_female.append('小姐的名字？')
namelist_question_female.append('乘客姓名？')
namelist_question_female.append('姓名？')
namelist_question_female.append('名字？')
namelist_question_female.append('小姐芳名可否见告？')
namelist_question_female.append('小姐的名字？')

namelist_question_male = []
namelist_question_male.append('您好，请问先生您的姓名是？')
namelist_question_male.append('请问先生怎么称呼？')
namelist_question_male.append('请问先生的姓名是？')
namelist_question_male.append('请先生告诉我您的名字。')
namelist_question_male.append('请问先生您的名字是？')
namelist_question_male.append('请输入先生您的全名。')
namelist_question_male.append('您叫什么名字啊，先生。')
namelist_question_male.append('请告知您的名字，先生。')
namelist_question_male.append('请问先生尊姓大名？')
namelist_question_male.append('麻烦先生说一下您的姓名可以吗？')
namelist_question_male.append('麻烦说下您的名字？谢谢先生。')
namelist_question_male.append('先生，您的名字？')
namelist_question_male.append('先生您怎么称呼？')
namelist_question_male.append('先生您叫什么名字？')
namelist_question_male.append('先生的名字？')
namelist_question_male.append('可否请教先生姓名？')

namelist_question_unisex = []
namelist_question_unisex.append('您好，请问您的姓名是？')
namelist_question_unisex.append('请问您的姓名是？')
namelist_question_unisex.append('请告诉我您的姓名')
namelist_question_unisex.append('请您告诉我您的名字。')
namelist_question_unisex.append('请问您要购买机票的用户姓名是？')
namelist_question_unisex.append('请问您的名字是？')
namelist_question_unisex.append('请告知您的姓名。')
namelist_question_unisex.append('我们需要知道您的姓名。')
namelist_question_unisex.append('您怎么称呼？')
namelist_question_unisex.append('您的全名是什么？')
namelist_question_unisex.append('请提供您的全名。')
namelist_question_unisex.append('请输入您的全名。')
namelist_question_unisex.append('您叫什么名字啊？')
namelist_question_unisex.append('您的名字是什么？')
namelist_question_unisex.append('请告知您的名字。')
namelist_question_unisex.append('请问尊姓大名？')
namelist_question_unisex.append('请输入乘客姓名。')
namelist_question_unisex.append('乘客的名字是什么？')
namelist_question_unisex.append('乘客怎么称呼？')
namelist_question_unisex.append('乘客叫什么名字？')
namelist_question_unisex.append('乘客的姓名是？')
namelist_question_unisex.append('麻烦您说一下您的姓名可以吗？')
namelist_question_unisex.append('麻烦说下您的名字？谢谢。')
namelist_question_unisex.append('请告知姓名，谢谢。')
namelist_question_unisex.append('麻烦您告诉我您的名字，非常感谢。')
namelist_question_unisex.append('您的名字？')
namelist_question_unisex.append('乘客姓名？')
namelist_question_unisex.append('姓名？')
namelist_question_unisex.append('名字？')

namelist_question_female_split = []
for ans in namelist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_female_split.append(w_sent)

namelist_question_male_split = []
for ans in namelist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_male_split.append(w_sent)

namelist_question_unisex_split = []
for ans in namelist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    namelist_question_unisex_split.append(w_sent)

namelist_question_female_split += namelist_question_unisex_split
namelist_question_male_split += namelist_question_unisex_split
pass
