# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

greetinglist_server = []
greetinglist_server.append('您好，宾馆前台，需要我为您做些什么？')
greetinglist_server.append('您好，这里是宾馆客服中心，需要什么服务？')
greetinglist_server.append('您好，我是宾馆预订服务员，需要什么服务？')
greetinglist_server.append('您好，这里是宾馆预订服务中心。')
greetinglist_server.append('您好，这里是宾馆预订服务中心，需要我为您做些什么？')
greetinglist_server.append('您好，这里是宾馆预订服务中心，需要什么帮助？')

greetinglist_server.append('上午好，宾馆前台，需要我为您做些什么？')
greetinglist_server.append('上午好，这里是宾馆客服中心，需要什么服务？')
greetinglist_server.append('上午好，我是宾馆预订服务员，需要什么服务？')
greetinglist_server.append('上午好，这里是宾馆预订服务中心。')
greetinglist_server.append('上午好，这里是宾馆预订服务中心，需要我为您做些什么？')
greetinglist_server.append('上午好，这里是宾馆预订服务中心，需要什么帮助？')

greetinglist_server.append('下午好，宾馆前台，需要我为您做些什么？')
greetinglist_server.append('下午好，这里是宾馆客服中心，需要什么服务？')
greetinglist_server.append('下午好，我是宾馆预订服务员，需要什么服务？')
greetinglist_server.append('下午好，这里是宾馆预订服务中心。')
greetinglist_server.append('下午好，这里是宾馆预订服务中心，需要我为您做些什么？')
greetinglist_server.append('下午好，这里是宾馆预订服务中心，需要什么帮助？')

greetinglist_client = []
greetinglist_client.append('我想预订宾馆')
greetinglist_client.append('我要预订房间。')
greetinglist_client.append('请帮我预订房间')
greetinglist_client.append('请您帮我预订一下宾馆房间。')
greetinglist_client.append('我需要预订房间。')
greetinglist_client.append('您好，我需要预订宾馆')
greetinglist_client.append('您好，我想预订宾馆')
greetinglist_client.append('您好，我要预订宾馆。')
greetinglist_client.append('您好，请帮我预订房间')
greetinglist_client.append('您好，请您帮我预订一下房间。')
greetinglist_client.append('您好，我需要预订宾馆。')

greetinglist_server_split = []
for ans in greetinglist_server:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_server_split.append(w_sent)

greetinglist_client_split = []
for ans in greetinglist_client:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_client_split.append(w_sent)
pass
