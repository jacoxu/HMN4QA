# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

idnumberlist_answer = []
idnumberlist_answer.append('秘密')
idnumberlist_answer.append('秘密')
idnumberlist_answer.append('秘密')

idnumberlist_answer.append('秘密。')
idnumberlist_answer.append('秘密。')
idnumberlist_answer.append('秘密。')
idnumberlist_answer.append('号码秘密。')
idnumberlist_answer.append('秘密我的号码。')
idnumberlist_answer.append('身份证秘密。')
idnumberlist_answer.append('身份证号码是秘密。')
idnumberlist_answer.append('身份证号秘密。')
idnumberlist_answer.append('秘密是我的身份证。')
idnumberlist_answer.append('等我想想。秘密。')
idnumberlist_answer.append('知道了，我的证件号码是秘密。')
idnumberlist_answer.append('号码应该是秘密。')

idnumberlist_answer.append('我的身份证号是秘密。')
idnumberlist_answer.append('是秘密。')
idnumberlist_answer.append('额，是秘密。')
idnumberlist_answer.append('啊，秘密。')
idnumberlist_answer.append('身份证号码是秘密。')
idnumberlist_answer.append('我的身份证是秘密。')

idnumberlist_answer.append('我的身份证号码是秘密')
idnumberlist_answer.append('号码是秘密')
idnumberlist_answer.append('你记一下，秘密')
idnumberlist_answer.append('我的身份证号是秘密')
idnumberlist_answer.append('我的身份证秘密')
idnumberlist_answer.append('身份证号秘密')
idnumberlist_answer.append('你记一下我的号码秘密')
idnumberlist_answer.append('请记一下我的身份证号码秘密')
idnumberlist_answer.append('秘密，这是我的号码')
idnumberlist_answer.append('秘密，我的号码')


idnumberlist_answer_split = []
for ans in idnumberlist_answer:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    w_sent = w_sent.replace('秘密'.decode('utf8'), '[slot_idnumber]')
    idnumberlist_answer_split.append(w_sent)
pass
