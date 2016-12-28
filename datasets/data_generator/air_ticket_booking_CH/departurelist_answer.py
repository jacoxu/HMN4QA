# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

departurelist_answer = []
departurelist_answer.append('北京')#这里的trick是加大一下常用句式的比重
departurelist_answer.append('北京')
departurelist_answer.append('北京')
departurelist_answer.append('额，北京')
departurelist_answer.append('北京。')
departurelist_answer.append('北京。')
departurelist_answer.append('北京。')
departurelist_answer.append('啊，是北京。')

departurelist_answer.append('从北京起飞。')
departurelist_answer.append('从北京出发的机票')
departurelist_answer.append('机票的出发地是北京。')
departurelist_answer.append('从北京出发。')
departurelist_answer.append('自北京出发。')
departurelist_answer.append('由北京起飞的飞机。')
departurelist_answer.append('出发地是北京。')
departurelist_answer.append('帮我预订北京起飞的机票。')
departurelist_answer.append('出行地点是北京。')
departurelist_answer.append('订从北京走的机票。')

departurelist_answer.append('我从北京出发')
departurelist_answer.append('出发地是北京')
departurelist_answer.append('我的出发地是北京')
departurelist_answer.append('我准备从北京出发')
departurelist_answer.append('我打算从北京出发')
departurelist_answer.append('我计划从北京出发')
departurelist_answer.append('我可能从北京出发')
departurelist_answer.append('从北京出发')
departurelist_answer.append('从北京走')
departurelist_answer.append('打算从北京走')
departurelist_answer.append('打算从北京出发')
departurelist_answer.append('准备从北京走')
departurelist_answer.append('准备从北京出发')

departurelist_answer_split = []

for ans in departurelist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('北京'.decode('utf8'), '[slot_departure]')
    departurelist_answer_split.append(w_sent)
pass
