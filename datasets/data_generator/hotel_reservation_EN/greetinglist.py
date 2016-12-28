# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

greetinglist_server = []
greetinglist_server.append('hi , hotel reception , what can i do for you ?')
greetinglist_server.append('hi , this is hotel service center , what services you need ?')
greetinglist_server.append('hello , i am the hotel receptionist , what services you need ?')
greetinglist_server.append('hello , this is hotel booking center .')
greetinglist_server.append('hello , hotel service center , how can i help you ?')
greetinglist_server.append('hello , this is hotel service center . what can i do for you ?')
greetinglist_server.append('hi , this is hotel booking center , what help you need ?')
greetinglist_server.append('hi , hotel reception , may i help you ?')

greetinglist_server.append('good morning , hotel reception , what can i do for you ?')
greetinglist_server.append('good morning , this is hotel service center , what services you need ?')
greetinglist_server.append('good morning , i am the hotel receptionist , what services you need ?')
greetinglist_server.append('good morning , this is hotel booking center .')
greetinglist_server.append('good morning , hotel service center , how can i help you ?')
greetinglist_server.append('good morning , this is hotel service center . what can i do for you ?')
greetinglist_server.append('good morning , this is hotel booking center , what help you need ?')
greetinglist_server.append('good morning , hotel reception , may i help you ?')

greetinglist_server.append('good afternoon , hotel reception , what can i do for you ?')
greetinglist_server.append('good afternoon , this is hotel service center , what services you need ?')
greetinglist_server.append('good afternoon , i am the hotel receptionist , what services you need ?')
greetinglist_server.append('good afternoon , this is hotel booking center .')
greetinglist_server.append('good afternoon , hotel service center , how can i help you ?')
greetinglist_server.append('good afternoon , this is hotel service center . what can i do for you ?')
greetinglist_server.append('good afternoon , this is hotel booking center , what help you need ?')
greetinglist_server.append('good afternoon , hotel reception , may i help you ?')

greetinglist_client = []
greetinglist_client.append('yeah , i would like to make a hotel reservation .')
greetinglist_client.append('yeah , i would like to make a hotel booking .')
greetinglist_client.append('yeah , i\'d like to reserve a hotel .')
greetinglist_client.append('yeah , i would like to book hotel .')
greetinglist_client.append('yeah , please make a reservation for me .')
greetinglist_client.append('yeah , i need to book a hotel .')
greetinglist_client.append('hello , i need to reserve a hotel .')
greetinglist_client.append('hi , i want to make hotel reservations .')
greetinglist_client.append('hello , i want to reserve a hotel .')
greetinglist_client.append('hi , please help me reserve a hotel .')
greetinglist_client.append('hi , please help me book a hotel .')
greetinglist_client.append('hello , i need to book a hotel .')
greetinglist_client.append('i would like to book a hotel .')
greetinglist_client.append('please make a reservation for me .')
greetinglist_client.append('i need to book a hotel .')
greetinglist_client.append('i need to reserve a hotel .')
greetinglist_client.append('i want to make hotel reservations .')
greetinglist_client.append('i need to make hotel reservations .')
greetinglist_client.append('i want to reserve a hotel .')

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
