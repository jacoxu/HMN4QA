# -*- coding: utf8 -*-
"""
    The data generator of task_01 for HMN4QA
    COLING2016 - Hierarchical Memory Networks for Answer Selection on Unknown Words
"""

import random
import datetime
from config import familyName_ch, firstName_female_ch, firstName_male_ch, locationDict_ch
from air_ticket_booking_CH.namelist_question import namelist_question_female_split, namelist_question_male_split
from air_ticket_booking_CH.namelist_answer import namelist_answer_split
from air_ticket_booking_CH.departurelist_question import departurelist_question_female_split, \
    departurelist_question_male_split
from air_ticket_booking_CH.departurelist_answer import departurelist_answer_split
from air_ticket_booking_CH.destinationlist_question import destinationlist_question_female_split, \
    destinationlist_question_male_split
from air_ticket_booking_CH.destinationlist_answer import destinationlist_answer_split
from air_ticket_booking_CH.timelist_question import timelist_question_female_split, timelist_question_male_split
from air_ticket_booking_CH.timelist_answer import timelist_answer_split
from air_ticket_booking_CH.idnumberlist_question import idnumberlist_question_female_split, \
    idnumberlist_question_male_split
from air_ticket_booking_CH.idnumberlist_answer import idnumberlist_answer_split
from air_ticket_booking_CH.phonelist_question import phonelist_question_female_split, phonelist_question_male_split
from air_ticket_booking_CH.phonelist_answer import phonelist_answer_split
from air_ticket_booking_CH.greetinglist import greetinglist_server_split, greetinglist_client_split
from air_ticket_booking_CH.endinglist import endinglist_server_female_split, endinglist_server_male_split, \
    endinglist_client_split
# for reproducibility
random.seed(1)
__author__ = '[jacoxu](https://github.com/jacoxu) & [shin](https://github.com/shincling)'

storyNumber = 1000
fw_qa_train = open('./task_01_air_ticket_booking_CH_train.txt', 'w')
fw_qa_dev = open('./task_01_air_ticket_booking_CH_dev.txt', 'w')
fw_qa_test = open('./task_01_air_ticket_booking_CH_test.txt', 'w')


def name_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(namelist_question_female_split)
        fullname = random.choice(familyName_ch) + random.choice(firstName_female_ch)
    else:
        tmp_q = random.choice(namelist_question_male_split)
        fullname = random.choice(familyName_ch) + random.choice(firstName_male_ch)
    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1
    ans_sent = random.choice(namelist_answer_split).replace('[slot_name]', fullname.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fullname


def departure_part(f, ind, gender, location):
    if gender == 0:
        tmp_q = random.choice(departurelist_question_female_split)
    else:
        tmp_q = random.choice(departurelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1
    fulldeparture = random.choice(locationDict_ch[location])
    ans_sent = random.choice(departurelist_answer_split).replace('[slot_departure]', fulldeparture.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fulldeparture


def destination_part(f, ind, gender, location):
    if gender == 0:
        tmp_q = random.choice(destinationlist_question_female_split)
    else:
        tmp_q = random.choice(destinationlist_question_male_split)

    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1
    fulldestination = random.choice(locationDict_ch[location])
    ans_sent = random.choice(destinationlist_answer_split).replace('[slot_destination]', fulldestination.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fulldestination


def time_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(timelist_question_female_split)
    else:
        tmp_q = random.choice(timelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1

    delta = datetime.timedelta(days=random.randint(-250, 250), seconds=random.randint(0, 59), microseconds=0,
                               milliseconds=0, minutes=random.randint(0, 59), hours=random.randint(0, 23), weeks=0)
    timetime = datetime.datetime.now()+delta
    fulltime = timetime.strftime('%Y年%m月%d日%H点')

    ans_sent = random.choice(timelist_answer_split).replace('[slot_time]', fulltime.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fulltime


def idnumber_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(idnumberlist_question_female_split)
        idnumber_check = random.choice([0, 2, 4, 6, 8])
    else:
        tmp_q = random.choice(idnumberlist_question_male_split)
        idnumber_check = random.choice([1, 3, 5, 7, 9])

    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1
    fullidnumber = str(random.randint(110100, 110113)) + str(random.randint(1940000000, 2001000000)) \
                   + str(idnumber_check) + str(random.randint(0, 9))
    ans_sent = random.choice(idnumberlist_answer_split).replace('[slot_idnumber]', fullidnumber.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fullidnumber


def phone_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(phonelist_question_female_split)
    else:
        tmp_q = random.choice(phonelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q.encode('utf8')))
    ind += 1
    fullphone = str(random.randint(13000000000, 13999999999))
    ans_sent = random.choice(phonelist_answer_split).replace('[slot_phone]', fullphone.decode('utf8'))
    f.write('%d%s' % (ind, ans_sent.encode('utf8')))
    ind += 1
    return ind, fullphone


def greeting_part(f, ind):
    greetinglist_server = random.choice(greetinglist_server_split)
    greetinglist_client = random.choice(greetinglist_client_split)

    f.write('%d%s' % (ind, greetinglist_server.encode('utf8')))
    ind += 1
    f.write('%d%s' % (ind, greetinglist_client.encode('utf8')))
    ind += 1
    return ind


def ending_part(f, ind, gender):
    if gender == 0:
        endinglist_server = random.choice(endinglist_server_female_split)
    else:
        endinglist_server = random.choice(endinglist_server_male_split)

    endinglist_client = random.choice(endinglist_client_split)

    f.write('%d%s' % (ind, endinglist_server.encode('utf8')))
    ind += 1
    f.write('%d%s' % (ind, endinglist_client.encode('utf8')))
    ind += 1
    return ind

orderlist = [0, 1, 2, 3, 4, 5]
genderlist = [0, 1]
locationlist = [0, 1]

# for train dataset
for story_ind in range(int(storyNumber * 0.9)):
    random.shuffle(orderlist)
    random.shuffle(genderlist)
    gender_client = genderlist[0]
    random.shuffle(locationlist)
    line_ind_qa = 1
    '''---------------greeting--------------'''
    line_ind_qa = greeting_part(fw_qa_train, line_ind_qa)
    '''---------------greeting--------------'''
    for i in orderlist:
        if i == 0:
            line_ind_qa, name = name_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 1:
            line_ind_qa, departure = departure_part(fw_qa_train, line_ind_qa, gender_client, locationlist[0])
            continue
        if i == 2:
            line_ind_qa, destination = destination_part(fw_qa_train, line_ind_qa, gender_client, locationlist[1])
            continue
        if i == 3:
            line_ind_qa, time = time_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, idnumber = idnumber_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_train, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_train, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_train.write('%d 订票 人 的 姓名 叫 什么 ？\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_train.write('%d 出发 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 1, departure, line_ind_qa - 1))
    fw_qa_train.write('%d 到达 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 2, destination, line_ind_qa - 1))
    fw_qa_train.write('%d 出发 时间 是 什么 时候 ？\t%s\t%d\n' % (line_ind_qa + 3, time, line_ind_qa - 1))
    fw_qa_train.write('%d 证件号码 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 4, idnumber, line_ind_qa - 1))
    fw_qa_train.write('%d 联系电话 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

fw_qa_train.close()
print 'It\'s done for train'
# for dev dataset
for story_ind in range(int(storyNumber * 0.1)):
    random.shuffle(orderlist)
    random.shuffle(genderlist)
    gender_client = genderlist[0]
    random.shuffle(locationlist)
    line_ind_qa = 1
    '''---------------greeting--------------'''
    line_ind_qa = greeting_part(fw_qa_dev, line_ind_qa)
    '''---------------greeting--------------'''
    for i in orderlist:
        if i == 0:
            line_ind_qa, name = name_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 1:
            line_ind_qa, departure = departure_part(fw_qa_dev, line_ind_qa, gender_client, locationlist[0])
            continue
        if i == 2:
            line_ind_qa, destination = destination_part(fw_qa_dev, line_ind_qa, gender_client, locationlist[1])
            continue
        if i == 3:
            line_ind_qa, time = time_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, idnumber = idnumber_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_dev, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_dev, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_dev.write('%d 订票 人 的 姓名 叫 什么 ？\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_dev.write('%d 出发 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 1, departure, line_ind_qa - 1))
    fw_qa_dev.write('%d 到达 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 2, destination, line_ind_qa - 1))
    fw_qa_dev.write('%d 出发 时间 是 什么 时候 ？\t%s\t%d\n' % (line_ind_qa + 3, time, line_ind_qa - 1))
    fw_qa_dev.write('%d 证件号码 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 4, idnumber, line_ind_qa - 1))
    fw_qa_dev.write('%d 联系电话 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

fw_qa_dev.close()
print 'It\'s done for dev'
# for test dataset
for story_ind in range(storyNumber):
    random.shuffle(orderlist)
    random.shuffle(genderlist)
    gender_client = genderlist[0]
    random.shuffle(locationlist)
    line_ind_qa = 1
    '''---------------greeting--------------'''
    line_ind_qa = greeting_part(fw_qa_test, line_ind_qa)
    '''---------------greeting--------------'''
    for i in orderlist:
        if i == 0:
            line_ind_qa, name = name_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 1:
            line_ind_qa, departure = departure_part(fw_qa_test, line_ind_qa, gender_client, locationlist[0])
            continue
        if i == 2:
            line_ind_qa, destination = destination_part(fw_qa_test, line_ind_qa, gender_client, locationlist[1])
            continue
        if i == 3:
            line_ind_qa, time = time_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, idnumber = idnumber_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_test, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_test, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_test.write('%d 订票 人 的 姓名 叫 什么 ？\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_test.write('%d 出发 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 1, departure, line_ind_qa - 1))
    fw_qa_test.write('%d 到达 城市 是 哪里 ？\t%s\t%d\n' % (line_ind_qa + 2, destination, line_ind_qa - 1))
    fw_qa_test.write('%d 出发 时间 是 什么 时候 ？\t%s\t%d\n' % (line_ind_qa + 3, time, line_ind_qa - 1))
    fw_qa_test.write('%d 证件号码 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 4, idnumber, line_ind_qa - 1))
    fw_qa_test.write('%d 联系电话 是 多少 ？\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

fw_qa_test.close()
print 'It\'s done for test'
