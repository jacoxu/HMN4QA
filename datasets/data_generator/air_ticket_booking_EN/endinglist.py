# -*- coding: utf8 -*-
__author__ = 'shin & jacoxu'

endinglist_server_female = []
endinglist_server_female.append('now you have been booked , miss .')
endinglist_server_female.append('ok miss , i was able to find an inexpensive flight for you .')
endinglist_server_female.append('well miss , i have you booked on a flight that will fit your schedule .')
endinglist_server_female.append('miss , i have you booked on a flight .')
endinglist_server_female.append('ok miss , the ticket has been reserved for you .')

endinglist_server_female.append('we have reserved for you , miss .')
endinglist_server_female.append('ok miss , have reserved for you .')
endinglist_server_female.append('ok miss , it\'s done .')
endinglist_server_female.append('done , the ticket has been reserved for you , miss .')

endinglist_server_male = []
endinglist_server_male.append('now you have been booked , sir .')
endinglist_server_male.append('ok sir , i was able to find an inexpensive flight for you .')
endinglist_server_male.append('well sir , i have you booked on a flight that will fit your schedule .')
endinglist_server_male.append('sir , i have you booked on a flight .')
endinglist_server_male.append('ok sir , the ticket has been reserved for you .')

endinglist_server_male.append('we have reserved for you , sir .')
endinglist_server_male.append('ok sir , have reserved for you .')
endinglist_server_male.append('ok sir , it\'s done .')
endinglist_server_male.append('done , the ticket has been reserved for you , sir .')

endinglist_server_unisex = []
endinglist_server_unisex.append('now you have been booked .')
endinglist_server_unisex.append('ok , i was able to find an inexpensive flight for you .')
endinglist_server_unisex.append('well , i have you booked on a flight that will fit your schedule .')
endinglist_server_unisex.append('i have you booked on a flight .')
endinglist_server_unisex.append('ok , the ticket has been reserved for you .')

endinglist_server_unisex.append('we have reserved for you .')
endinglist_server_unisex.append('ok , have reserved for you .')
endinglist_server_unisex.append('ok , it\'s done .')
endinglist_server_unisex.append('done , the ticket has been reserved for you .')

endinglist_client = []
endinglist_client.append('so fast , thanks very much .')
endinglist_client.append('ah , ok , thanks .')
endinglist_client.append('well , good , thanks very much .')
endinglist_client.append('hmm , thanks for you service .')
endinglist_client.append('ha , thanks for your service !')
endinglist_client.append('good , thanks .')
endinglist_client.append('ok , thank you .')
endinglist_client.append('wonderful , thanks for your service .')
endinglist_client.append('eh , ok , thanks for your service .')
endinglist_client.append('wonderful , thank you .')
endinglist_client.append('thanks very much !')
endinglist_client.append('thanks very much .')
endinglist_client.append('thanks very much')

endinglist_server_female_split = []
for ans in endinglist_server_female:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_server_female_split.append(w_sent)

endinglist_server_male_split = []
for ans in endinglist_server_male:
    w_sent = ''
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_server_male_split.append(w_sent)

endinglist_server_unisex_split = []
for ans in endinglist_server_unisex:
    w_sent = ''
    sent = ans.split(' ')
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
    sent = ans.split(' ')
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    endinglist_client_split.append(w_sent)
pass
