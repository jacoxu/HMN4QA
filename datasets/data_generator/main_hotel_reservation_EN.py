# -*- coding: utf8 -*-
"""
    The data generator of task_04 for HMN4QA
    COLING2016 - Hierarchical Memory Networks for Answer Selection on Unknown Words
"""

import random
import datetime
from config import familyName_en, firstName_female_en, firstName_male_en, roomtypeDict_en, roomcountDict_en
from hotel_reservation_EN.namelist_question import namelist_question_female_split, namelist_question_male_split
from hotel_reservation_EN.namelist_answer import namelist_answer_split
from hotel_reservation_EN.roomtypelist_question import roomtpyelist_question_female_split, \
    roomtypelist_question_male_split
from hotel_reservation_EN.roomtypelist_answer import roomtypelist_answer_split
from hotel_reservation_EN.countlist_question import countlist_question_female_split, countlist_question_male_split
from hotel_reservation_EN.countlist_answer import countlist_answer_split
from hotel_reservation_EN.timelist_question import timelist_question_female_split, timelist_question_male_split
from hotel_reservation_EN.timelist_answer import timelist_answer_split
from hotel_reservation_EN.idnumberlist_question import idnumberlist_question_female_split, \
    idnumberlist_question_male_split
from hotel_reservation_EN.idnumberlist_answer import idnumberlist_answer_split
from hotel_reservation_EN.phonelist_question import phonelist_question_female_split, phonelist_question_male_split
from hotel_reservation_EN.phonelist_answer import phonelist_answer_split
from hotel_reservation_EN.greetinglist import greetinglist_server_split, greetinglist_client_split
from hotel_reservation_EN.endinglist import endinglist_server_female_split, endinglist_server_male_split, \
    endinglist_client_split
# for reproducibility
random.seed(4)
__author__ = '[jacoxu](https://github.com/jacoxu) & [shin](https://github.com/shincling)'

storyNumber = 1000
fw_qa_train = open('./task_04_hotel_reservation_EN_train.txt', 'w')
fw_qa_dev = open('./task_04_hotel_reservation_EN_dev.txt', 'w')
fw_qa_test = open('./task_04_hotel_reservation_EN_test.txt', 'w')


def name_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(namelist_question_female_split)
        fullname = random.choice(firstName_female_en) + '_' + random.choice(familyName_en)
    else:
        tmp_q = random.choice(namelist_question_male_split)
        fullname = random.choice(firstName_male_en) + '_' + random.choice(familyName_en)
    f.write('%d%s' % (ind, tmp_q))
    ind += 1
    ans_sent = random.choice(namelist_answer_split).replace('[slot_name]', fullname)
    f.write('%d%s' % (ind, ans_sent))
    ind += 1
    return ind, fullname


def room_type(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(roomtpyelist_question_female_split)
    else:
        tmp_q = random.choice(roomtypelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q))
    ind += 1
    fullroomtype = random.choice(roomtypeDict_en)
    ans_sent = random.choice(roomtypelist_answer_split).replace('[slot_roomtype]', fullroomtype)
    f.write('%d%s' % (ind, ans_sent))
    ind += 1
    return ind, fullroomtype


def count_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(countlist_question_female_split)
    else:
        tmp_q = random.choice(countlist_question_male_split)

    f.write('%d%s' % (ind, tmp_q))
    ind += 1
    rand_or_rule = random.randint(0, 5)
    if rand_or_rule > 3:
        fullcount = str(random.randint(1, 200))
    else:
        fullcount = random.choice(roomcountDict_en)
    ans_sent = random.choice(countlist_answer_split).replace('[slot_count]', fullcount)
    if fullcount != '1' or fullcount != 'one':
        ans_sent = ans_sent.replace('room', 'rooms')
    f.write('%d%s' % (ind, ans_sent))
    ind += 1
    return ind, fullcount


def time_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(timelist_question_female_split)
    else:
        tmp_q = random.choice(timelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q))
    ind += 1

    delta = datetime.timedelta(days=random.randint(-1000, 1000), seconds=random.randint(0, 59), microseconds=0,
                               milliseconds=0, minutes=random.randint(0, 59), hours=random.randint(0, 23), weeks=0)
    timetime = datetime.datetime.now()+delta
    tmptime = timetime.day
    if tmptime <= 12:
        delta_day = datetime.timedelta(days=random.randint(12, 16))
        timetime = datetime.datetime.now()+delta+delta_day
    fulltime = timetime.strftime('%m/%d/%Y')

    ans_sent = random.choice(timelist_answer_split).replace('[slot_time]', fulltime)
    f.write('%d%s' % (ind, ans_sent))
    ind += 1
    return ind, fulltime


def idnumber_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(idnumberlist_question_female_split)
    else:
        tmp_q = random.choice(idnumberlist_question_male_split)

    f.write('%d%s' % (ind, tmp_q))
    ind += 1
    fullidnumber = str(random.randint(124000000, 900100000))
    ans_sent = random.choice(idnumberlist_answer_split).replace('[slot_idnumber]', fullidnumber)
    f.write('%d%s' % (ind, ans_sent))
    ind += 1
    return ind, fullidnumber


def phone_part(f, ind, gender):
    if gender == 0:
        tmp_q = random.choice(phonelist_question_female_split)
    else:
        tmp_q = random.choice(phonelist_question_male_split)

    f.write('%d%s' % (ind, tmp_q))
    ind += 1
    fullphone = '001617' + str(random.randint(1000010, 8945158))
    ans_sent = random.choice(phonelist_answer_split).replace('[slot_phone]', fullphone)
    f.write('%d%s' % (ind, ans_sent))
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
            line_ind_qa, time = time_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 2:
            line_ind_qa, idnumber = idnumber_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 3:
            line_ind_qa, roomtype = room_type(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, count = count_part(fw_qa_train, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_train, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_train, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_train.write('%d what is the client\'s name ?\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_train.write('%d when does the client check in ?\t%s\t%d\n' % (line_ind_qa + 1, time, line_ind_qa - 1))
    fw_qa_train.write('%d what is the passport number ?\t%s\t%d\n' % (line_ind_qa + 2, idnumber, line_ind_qa - 1))
    fw_qa_train.write('%d what is the room type ?\t%s\t%d\n' % (line_ind_qa + 3, roomtype, line_ind_qa - 1))
    fw_qa_train.write('%d how many rooms does the client book ?\t%s\t%d\n' % (line_ind_qa + 4, count, line_ind_qa - 1))
    fw_qa_train.write('%d what is the contact number ?\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

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
            line_ind_qa, time = time_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 2:
            line_ind_qa, idnumber = idnumber_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 3:
            line_ind_qa, roomtype = room_type(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, count = count_part(fw_qa_dev, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_dev, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_dev, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_dev.write('%d what is the client\'s name ?\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_dev.write('%d when does the client check in ?\t%s\t%d\n' % (line_ind_qa + 1, time, line_ind_qa - 1))
    fw_qa_dev.write('%d what is the passport number ?\t%s\t%d\n' % (line_ind_qa + 2, idnumber, line_ind_qa - 1))
    fw_qa_dev.write('%d what is the room type ?\t%s\t%d\n' % (line_ind_qa + 3, roomtype, line_ind_qa - 1))
    fw_qa_dev.write('%d how many rooms does the client book ?\t%s\t%d\n' % (line_ind_qa + 4, count, line_ind_qa - 1))
    fw_qa_dev.write('%d what is the contact number ?\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

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
            line_ind_qa, time = time_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 2:
            line_ind_qa, idnumber = idnumber_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 3:
            line_ind_qa, roomtype = room_type(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 4:
            line_ind_qa, count = count_part(fw_qa_test, line_ind_qa, gender_client)
            continue
        if i == 5:
            line_ind_qa, phone = phone_part(fw_qa_test, line_ind_qa, gender_client)
            continue

    '''---------------ending--------------'''
    line_ind_qa = ending_part(fw_qa_test, line_ind_qa, gender_client)
    '''---------------ending--------------'''

    fw_qa_test.write('%d what is the client\'s name ?\t%s\t%d\n' % (line_ind_qa, name, line_ind_qa - 1))
    fw_qa_test.write('%d when does the client check in ?\t%s\t%d\n' % (line_ind_qa + 1, time, line_ind_qa - 1))
    fw_qa_test.write('%d what is the passport number ?\t%s\t%d\n' % (line_ind_qa + 2, idnumber, line_ind_qa - 1))
    fw_qa_test.write('%d what is the room type ?\t%s\t%d\n' % (line_ind_qa + 3, roomtype, line_ind_qa - 1))
    fw_qa_test.write('%d how many rooms does the client book ?\t%s\t%d\n' % (line_ind_qa + 4, count, line_ind_qa - 1))
    fw_qa_test.write('%d what is the contact number ?\t%s\t%d\n' % (line_ind_qa + 5, phone, line_ind_qa - 1))

fw_qa_test.close()
print 'It\'s done for test'
