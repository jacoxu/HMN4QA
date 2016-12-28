# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

endinglist_server_female = []
endinglist_server_female.append('小姐您好，已经为您预订完毕。')
endinglist_server_female.append('女士您好，已经为您预订完毕。')
endinglist_server_female.append('好了，已经为女士预订完毕。')
endinglist_server_female.append('可以了小姐，已帮您成功预订。')
endinglist_server_female.append('小姐，已经帮您预订好了。')
endinglist_server_female.append('女士，您所需要的机票已经预订成功。')

endinglist_server_female.append('小姐，我们已经成功为您预订。')
endinglist_server_female.append('感谢女士配合，我们已经成功为您预订。')
endinglist_server_female.append('好的小姐，已经为您预订成功。')
endinglist_server_female.append('已经为您预订成功了，小姐。')
endinglist_server_female.append('小姐您好，已经为您成功为您下单。')
endinglist_server_female.append('可以了，机票为您预订成功，小姐。')

endinglist_server_male = []
endinglist_server_male.append('先生您好，已经为您预订完毕。')
endinglist_server_male.append('先生您好，已经为您预订完毕。')
endinglist_server_male.append('好了，已经为先生预订完毕。')
endinglist_server_male.append('可以了先生，已帮您成功预订。')
endinglist_server_male.append('先生，已经帮您预订好了。')
endinglist_server_male.append('先生，您所需要的机票已经预订成功。')

endinglist_server_male.append('先生，我们已经成功为您预订。')
endinglist_server_male.append('感谢先生配合，我们已经成功为您预订。')
endinglist_server_male.append('好的先生，已经为您预订成功。')
endinglist_server_male.append('已经为您预订成功了，先生。')
endinglist_server_male.append('先生您好，已经为您成功为您下单。')
endinglist_server_male.append('可以了，机票为您预订成功，先生。')

endinglist_server_unisex = []
endinglist_server_unisex.append('您好，已经为您预订完毕。')
endinglist_server_unisex.append('您好，已经为您预订完毕。')
endinglist_server_unisex.append('好了，已经为预订完毕。')
endinglist_server_unisex.append('可以了，已帮您成功预订。')
endinglist_server_unisex.append('已经帮您预订好了。')
endinglist_server_unisex.append('您所需要的机票已经预订成功。')

endinglist_server_unisex.append('我们已经成功为您预订。')
endinglist_server_unisex.append('感谢配合，我们已经成功为您预订。')
endinglist_server_unisex.append('好的，已经为您预订成功。')
endinglist_server_unisex.append('已经为您预订成功了。')
endinglist_server_unisex.append('您好，已经为您成功为您下单。')
endinglist_server_unisex.append('可以了，机票为您预订成功。')

endinglist_client = []
endinglist_client.append('这么快，非常感谢您')
endinglist_client.append('啊，好的，非常感谢。')
endinglist_client.append('好的好的，非常感谢。')
endinglist_client.append('嗯好的，谢谢您的服务。')
endinglist_client.append('嗯哈，感谢您的服务')
endinglist_client.append('太好了，谢谢您')
endinglist_client.append('好，谢谢您')
endinglist_client.append('太好了，谢谢您的服务。')
endinglist_client.append('恩好，感谢您的服务')
endinglist_client.append('好开心，谢谢您！')
endinglist_client.append('非常感谢！')
endinglist_client.append('非常感谢。')
endinglist_client.append('非常感谢')

endinglist_server_female_split = []
for ans in endinglist_server_female:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_server_female_split.append(w_sent)

endinglist_server_male_split = []
for ans in endinglist_server_male:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_server_male_split.append(w_sent)

endinglist_server_unisex_split = []
for ans in endinglist_server_unisex:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_server_unisex_split.append(w_sent)

endinglist_server_female_split += endinglist_server_unisex_split
endinglist_server_male_split += endinglist_server_unisex_split

endinglist_client_split = []
for ans in endinglist_client:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_client_split.append(w_sent)
pass
