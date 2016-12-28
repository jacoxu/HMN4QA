# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'
import jieba

roomtpyelist_answer = []
roomtpyelist_answer.append('北京')
roomtpyelist_answer.append('北京')
roomtpyelist_answer.append('北京')
roomtpyelist_answer.append('额，北京')
roomtpyelist_answer.append('北京。')
roomtpyelist_answer.append('北京。')
roomtpyelist_answer.append('北京。')
roomtpyelist_answer.append('啊，要北京。')

roomtpyelist_answer.append('预订北京。')
roomtpyelist_answer.append('我要订北京')
roomtpyelist_answer.append('我想预订北京。')
roomtpyelist_answer.append('北京就行。')
roomtpyelist_answer.append('要北京就行。')
roomtpyelist_answer.append('预订北京就好。')
roomtpyelist_answer.append('房间类型是北京。')
roomtpyelist_answer.append('帮我预订北京吧。')
roomtpyelist_answer.append('帮我订北京')
roomtpyelist_answer.append('订北京就可以了。')

roomtpyelist_answer.append('来北京吧')
roomtpyelist_answer.append('北京就好')
roomtpyelist_answer.append('帮我预订北京就行')
roomtpyelist_answer.append('北京就够了')
roomtpyelist_answer.append('我打算订北京')
roomtpyelist_answer.append('我需要北京')
roomtpyelist_answer.append('我需要预订北京')
roomtpyelist_answer.append('要北京')
roomtpyelist_answer.append('要北京。')
roomtpyelist_answer.append('额，帮我订北京吧。')
roomtpyelist_answer.append('帮我预订北京就够了。')
roomtpyelist_answer.append('北京就好。')
roomtpyelist_answer.append('订北京就可以了，谢谢')

roomtypelist_answer_split = []

for ans in roomtpyelist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('北京'.decode('utf8'), '[slot_roomtype]')
    roomtypelist_answer_split.append(w_sent)
pass
