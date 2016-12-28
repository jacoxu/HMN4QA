# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

phonelist_question_female = []
phonelist_question_female.append('请问女士您的电话号码是多少？')
phonelist_question_female.append('请问女士您的电话号是？')
phonelist_question_female.append('小姐，请告诉我您的电话号码？')
phonelist_question_female.append('您好小姐，我需要输入您的电话号码。')
phonelist_question_female.append('请女士您告诉我您的电话号码。')
phonelist_question_female.append('小姐，请提供住客的电话号码。')
phonelist_question_female.append('小姐，住客的电话是？')
phonelist_question_female.append('小姐，您的电话是多少啊？')
phonelist_question_female.append('请女士您告诉我您的电话号码。')
phonelist_question_female.append('女士的电话号码是多少呢？')
phonelist_question_female.append('小姐，您电话多少？')
phonelist_question_female.append('小姐，您电话号码多少？')
phonelist_question_female.append('我们需要知道女士您的电话号。')
phonelist_question_female.append('小姐，电话？')
phonelist_question_female.append('小姐，电话号？')
phonelist_question_female.append('小姐，电话号码？')
phonelist_question_female.append('小姐，您电话的号码？')
phonelist_question_female.append('请告诉我您的电话号码，小姐。')
phonelist_question_female.append('小姐的电话号码是多少呢？')
phonelist_question_female.append('还需要提供电话，谢谢小姐。')
phonelist_question_female.append('电话号？谢谢小姐。')
phonelist_question_female.append('小姐，麻烦您说下电话号。')
phonelist_question_female.append('请问您电话，谢谢小姐。')
phonelist_question_female.append('好的女士，请告诉我您的电话号码，非常感谢。')
phonelist_question_female.append('没问题女士，您电话号码？')
phonelist_question_female.append('知道了女士，您电话的号码？')
phonelist_question_female.append('明白了女士，请告诉我您的电话号码。')
phonelist_question_female.append('好的，小姐的电话号码是多少呢？')
phonelist_question_female.append('了解了女士，还需要提供电话，谢谢。')
phonelist_question_female.append('嗯嗯，电话号？谢谢女士。')
phonelist_question_female.append('请问女士您的电话号码是多少？')
phonelist_question_female.append('小姐，请告诉我您的联系方式？')
phonelist_question_female.append('小姐，请问您的联系电话是？')
phonelist_question_female.append('小姐，请告诉我您的联系电话。')
phonelist_question_female.append('您好女士，我需要输入您的联系电话。')

phonelist_question_male = []
phonelist_question_male.append('请问先生您的电话号码是多少？')
phonelist_question_male.append('请问先生您的电话号是？')
phonelist_question_male.append('先生，请告诉我您的电话号码？')
phonelist_question_male.append('您好先生，我需要输入您的电话号码。')
phonelist_question_male.append('请先生您告诉我您的电话号码。')
phonelist_question_male.append('先生，请提供住客的电话号码。')
phonelist_question_male.append('先生，住客的电话是？')
phonelist_question_male.append('先生，您的电话是多少啊？')
phonelist_question_male.append('请先生您告诉我您的电话号码。')
phonelist_question_male.append('先生的电话号码是多少呢？')
phonelist_question_male.append('先生，您电话多少？')
phonelist_question_male.append('先生，您电话号码多少？')
phonelist_question_male.append('我们需要知道先生您的电话号。')
phonelist_question_male.append('先生，电话？')
phonelist_question_male.append('先生，电话号？')
phonelist_question_male.append('先生，电话号码？')
phonelist_question_male.append('先生，您电话的号码？')
phonelist_question_male.append('请告诉我您的电话号码，先生。')
phonelist_question_male.append('先生的电话号码是多少呢？')
phonelist_question_male.append('还需要提供电话，谢谢先生。')
phonelist_question_male.append('电话号？谢谢先生。')
phonelist_question_male.append('先生，麻烦您说下电话号。')
phonelist_question_male.append('请问您电话，谢谢先生。')
phonelist_question_male.append('好的先生，请告诉我您的电话号码，非常感谢。')
phonelist_question_male.append('没问题先生，您电话号码？')
phonelist_question_male.append('知道了先生，您电话的号码？')
phonelist_question_male.append('明白了先生，请告诉我您的电话号码。')
phonelist_question_male.append('好的，先生的电话号码是多少呢？')
phonelist_question_male.append('了解了先生，还需要提供电话，谢谢。')
phonelist_question_male.append('嗯嗯，电话号？谢谢先生。')
phonelist_question_male.append('请问先生您的电话号码是多少？')
phonelist_question_male.append('先生，请告诉我您的联系方式？')
phonelist_question_male.append('先生，请问您的联系电话是？')
phonelist_question_male.append('先生，请告诉我您的联系电话。')
phonelist_question_male.append('您好先生，我需要输入您的联系电话。')

phonelist_question_unisex = []
phonelist_question_unisex.append('请问您的电话号码是多少？')
phonelist_question_unisex.append('请问您的电话号是？')
phonelist_question_unisex.append('请告诉我您的电话号码？')
phonelist_question_unisex.append('您好，我需要输入您的电话号码。')
phonelist_question_unisex.append('请您告诉我您的电话号码。')
phonelist_question_unisex.append('请提供住客的电话号码。')
phonelist_question_unisex.append('住客的电话是？')
phonelist_question_unisex.append('您的电话是多少啊？')
phonelist_question_unisex.append('请您告诉我您的电话号码。')
phonelist_question_unisex.append('您电话多少？')
phonelist_question_unisex.append('您电话号码多少？')
phonelist_question_unisex.append('我们需要知道您的电话号。')
phonelist_question_unisex.append('电话？')
phonelist_question_unisex.append('电话号？')
phonelist_question_unisex.append('电话号码？')
phonelist_question_unisex.append('您电话的号码？')
phonelist_question_unisex.append('请告诉我您的电话号码。')
phonelist_question_unisex.append('还需要提供电话，谢谢。')
phonelist_question_unisex.append('电话号？谢谢。')
phonelist_question_unisex.append('麻烦您说下电话号。')
phonelist_question_unisex.append('请问您电话，谢谢。')
phonelist_question_unisex.append('好的，请告诉我您的电话号码，非常感谢。')
phonelist_question_unisex.append('没问题，您电话号码？')
phonelist_question_unisex.append('知道了，您电话的号码？')
phonelist_question_unisex.append('明白了，请告诉我您的电话号码。')
phonelist_question_unisex.append('了解了，还需要提供电话，谢谢。')
phonelist_question_unisex.append('嗯嗯，电话号？谢谢。')
phonelist_question_unisex.append('请问您的电话号码是多少？')
phonelist_question_unisex.append('请告诉我您的联系方式？')
phonelist_question_unisex.append('请问您的联系电话是？')
phonelist_question_unisex.append('请告诉我您的联系电话。')
phonelist_question_unisex.append('您好，我需要输入您的联系电话。')

phonelist_question_female_split = []
for ans in phonelist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_female_split.append(w_sent)

phonelist_question_male_split = []
for ans in phonelist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_male_split.append(w_sent)

phonelist_question_unisex_split = []
for ans in phonelist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    phonelist_question_unisex_split.append(w_sent)

phonelist_question_female_split += phonelist_question_unisex_split
phonelist_question_male_split += phonelist_question_unisex_split

pass
