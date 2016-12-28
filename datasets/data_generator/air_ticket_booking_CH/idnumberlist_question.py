# -*- coding: utf8 -*-
import jieba
__author__ = 'shin & jacoxu'

idnumberlist_question_female = []
idnumberlist_question_female.append('女士，请问您的身份证号码是多少？')
idnumberlist_question_female.append('请问女士您的身份证号是？')
idnumberlist_question_female.append('请告诉我小姐您的身份证号码？')
idnumberlist_question_female.append('女士您好，我需要输入您的身份证号码。')
idnumberlist_question_female.append('请小姐您告诉我您的身份证号码。')
idnumberlist_question_female.append('女士，请提供乘客的身份证号码。')
idnumberlist_question_female.append('小姐，乘客的身份证是？')
idnumberlist_question_female.append('女士，您的身份证是多少啊？')
idnumberlist_question_female.append('请女士您告诉我您的身份证号码。')
idnumberlist_question_female.append('小姐的身份证号码是多少呢？')
idnumberlist_question_female.append('小姐，您身份证多少？')
idnumberlist_question_female.append('小姐，您身份证号码多少？')
idnumberlist_question_female.append('女士，我们需要知道您的身份证号。')
idnumberlist_question_female.append('小姐，身份证？')
idnumberlist_question_female.append('女士，身份证号？')
idnumberlist_question_female.append('女士，身份证号码？')
idnumberlist_question_female.append('女士，身份证件？')
idnumberlist_question_female.append('女士，身份证件号码？')
idnumberlist_question_female.append('女士，您身份证的号码？')
idnumberlist_question_female.append('请女士告诉我您的身份证号码。')
idnumberlist_question_female.append('小姐的身份证号码是多少呢？')
idnumberlist_question_female.append('需要提供身份证件，谢谢女士。')
idnumberlist_question_female.append('身份证号？谢谢女士。')
idnumberlist_question_female.append('麻烦您说下身份证号，女士。')
idnumberlist_question_female.append('请问您身份证，谢谢女士。')
idnumberlist_question_female.append('好的女士，请告诉我您的身份证号码，非常感谢。')
idnumberlist_question_female.append('没问题小姐，您身份证件号码？')
idnumberlist_question_female.append('知道了女士，您身份证的号码？')
idnumberlist_question_female.append('明白了女士，请告诉我您的身份证号码。')
idnumberlist_question_female.append('好的，小姐的身份证号码是多少呢？')
idnumberlist_question_female.append('了解了，还需要提供身份证件，谢谢女士。')
idnumberlist_question_female.append('嗯嗯，身份证号？谢谢小姐。')

idnumberlist_question_male = []
idnumberlist_question_male.append('先生，请问您的身份证号码是多少？')
idnumberlist_question_male.append('请问先生您的身份证号是？')
idnumberlist_question_male.append('请告诉我先生您的身份证号码？')
idnumberlist_question_male.append('先生您好，我需要输入您的身份证号码。')
idnumberlist_question_male.append('请先生您告诉我您的身份证号码。')
idnumberlist_question_male.append('先生，请提供乘客的身份证号码。')
idnumberlist_question_male.append('先生，乘客的身份证是？')
idnumberlist_question_male.append('先生，您的身份证是多少啊？')
idnumberlist_question_male.append('请先生您告诉我您的身份证号码。')
idnumberlist_question_male.append('先生的身份证号码是多少呢？')
idnumberlist_question_male.append('先生，您身份证多少？')
idnumberlist_question_male.append('先生，您身份证号码多少？')
idnumberlist_question_male.append('先生，我们需要知道您的身份证号。')
idnumberlist_question_male.append('先生，身份证？')
idnumberlist_question_male.append('先生，身份证号？')
idnumberlist_question_male.append('先生，身份证号码？')
idnumberlist_question_male.append('先生，身份证件？')
idnumberlist_question_male.append('先生，身份证件号码？')
idnumberlist_question_male.append('先生，您身份证的号码？')
idnumberlist_question_male.append('请先生告诉我您的身份证号码。')
idnumberlist_question_male.append('先生的身份证号码是多少呢？')
idnumberlist_question_male.append('需要提供身份证件，谢谢先生。')
idnumberlist_question_male.append('身份证号？谢谢先生。')
idnumberlist_question_male.append('麻烦您说下身份证号，先生。')
idnumberlist_question_male.append('请问您身份证，谢谢先生。')
idnumberlist_question_male.append('好的先生，请告诉我您的身份证号码，非常感谢。')
idnumberlist_question_male.append('没问题先生，您身份证件号码？')
idnumberlist_question_male.append('知道了先生，您身份证的号码？')
idnumberlist_question_male.append('明白了先生，请告诉我您的身份证号码。')
idnumberlist_question_male.append('好的，先生的身份证号码是多少呢？')
idnumberlist_question_male.append('了解了，还需要提供身份证件，谢谢先生。')
idnumberlist_question_male.append('嗯嗯，身份证号？谢谢先生。')

idnumberlist_question_unisex = []
idnumberlist_question_unisex.append('请问您的身份证号码是多少？')
idnumberlist_question_unisex.append('请问您的身份证号是？')
idnumberlist_question_unisex.append('请告诉我您的身份证号码？')
idnumberlist_question_unisex.append('您好，我需要输入您的身份证号码。')
idnumberlist_question_unisex.append('请您告诉我您的身份证号码。')
idnumberlist_question_unisex.append('请提供乘客的身份证号码。')
idnumberlist_question_unisex.append('乘客的身份证是？')
idnumberlist_question_unisex.append('您的身份证是多少啊？')
idnumberlist_question_unisex.append('请您告诉我您的身份证号码。')
idnumberlist_question_unisex.append('您身份证多少？')
idnumberlist_question_unisex.append('您身份证号码多少？')
idnumberlist_question_unisex.append('我们需要知道您的身份证号。')
idnumberlist_question_unisex.append('身份证？')
idnumberlist_question_unisex.append('身份证号？')
idnumberlist_question_unisex.append('身份证号码？')
idnumberlist_question_unisex.append('身份证件？')
idnumberlist_question_unisex.append('身份证件号码？')
idnumberlist_question_unisex.append('您身份证的号码？')
idnumberlist_question_unisex.append('请告诉我您的身份证号码。')
idnumberlist_question_unisex.append('需要提供身份证件，谢谢。')
idnumberlist_question_unisex.append('身份证号？谢谢。')
idnumberlist_question_unisex.append('麻烦您说下身份证号。')
idnumberlist_question_unisex.append('请问您身份证，谢谢。')
idnumberlist_question_unisex.append('好的，请告诉我您的身份证号码，非常感谢。')
idnumberlist_question_unisex.append('没问题，您身份证件号码？')
idnumberlist_question_unisex.append('知道了，您身份证的号码？')
idnumberlist_question_unisex.append('明白了，请告诉我您的身份证号码。')
idnumberlist_question_unisex.append('了解了，还需要提供身份证件，谢谢。')
idnumberlist_question_unisex.append('嗯嗯，身份证号？谢谢。')

idnumberlist_question_female_split = []
for ans in idnumberlist_question_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_female_split.append(w_sent)

idnumberlist_question_male_split = []
for ans in idnumberlist_question_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_male_split.append(w_sent)

idnumberlist_question_unisex_split = []
for ans in idnumberlist_question_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    idnumberlist_question_unisex_split.append(w_sent)

pass
