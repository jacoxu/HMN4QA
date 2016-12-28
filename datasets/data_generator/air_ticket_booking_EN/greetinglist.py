# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

greetinglist_server = []
greetinglist_server.append('hi , air ticket booking center , what can i do for you ?')
greetinglist_server.append('hi , this is air ticket booking center , what services you need ?')
greetinglist_server.append('hello , i am the air ticket booking agent , what services you need ?')
greetinglist_server.append('hello , this is air ticket booking agent center .')
greetinglist_server.append('hello , air ticket booking agent center , how can i help you ?')
greetinglist_server.append('hello , this is air ticket booking agent center . what can i do for you ?')
greetinglist_server.append('hi , this is air ticket booking service center , what help you need ?')
greetinglist_server.append('hi , this is air ticket booking service center , may i help you ?')

greetinglist_server.append('good morning , air ticket booking center , what can i do for you ?')
greetinglist_server.append('good morning , this is air ticket booking center , what services you need ?')
greetinglist_server.append('good morning , i am the air ticket booking agent , what services you need ?')
greetinglist_server.append('good morning , this is air ticket booking agent center .')
greetinglist_server.append('good morning , this is air ticket booking agent center . what can i do for you ?')
greetinglist_server.append('good morning , this is air ticket booking service center , what help you need ?')
greetinglist_server.append('good morning , this is air ticket booking service center , may i help you ?')

greetinglist_server.append('good afternoon , air ticket booking center , what can i do for you ?')
greetinglist_server.append('good afternoon , this is air ticket booking center , what services you need ?')
greetinglist_server.append('good afternoon , i am the air ticket booking agent , what services you need ?')
greetinglist_server.append('good afternoon , this is air ticket booking agent center .')
greetinglist_server.append('good afternoon , this is air ticket booking agent center . what can i do for you ?')
greetinglist_server.append('good afternoon , this is air ticket booking service center , what help you need ?')
greetinglist_server.append('good afternoon , this is air ticket booking service center , may i help you ?')

greetinglist_client = []
greetinglist_client.append('yeah , i would like to make a flight reservation .')
greetinglist_client.append('yeah , i would like to make a flight booking .')
greetinglist_client.append('yeah , i\'d like to reserve a flight .')
greetinglist_client.append('yeah , i would like to book an air ticket .')
greetinglist_client.append('yeah , please make a reservation for me .')
greetinglist_client.append('yeah , i need to book an air ticket .')
greetinglist_client.append('hello , i need to reserve a flight .')
greetinglist_client.append('hi , i want to make flight reservations .')
greetinglist_client.append('hello , i want to reserve a seat .')
greetinglist_client.append('hi , please help me reserve a ticket .')
greetinglist_client.append('hi , please help me book an air ticket .')
greetinglist_client.append('hello , i need to book a plane ticket .')
greetinglist_client.append('i would like to book an air ticket .')
greetinglist_client.append('i would like to buy a plane ticket .')
greetinglist_client.append('please make a reservation for me .')
greetinglist_client.append('i need to book an air ticket .')
greetinglist_client.append('i need to reserve a flight .')
greetinglist_client.append('i would like to buy a plane ticket please .')
greetinglist_client.append('i\'d like to buy a ticket .')
greetinglist_client.append('i want to make flight reservations .')
greetinglist_client.append('i want to make plane reservations .')
greetinglist_client.append('i need to make plane reservations .')
greetinglist_client.append('i want to reserve a seat .')

greetinglist_server_split = []
for ans in greetinglist_server:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_server_split.append(w_sent)

greetinglist_client_split = []
for ans in greetinglist_client:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_client_split.append(w_sent)
pass
