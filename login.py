# !/usr/bin/python
#coding=utf-8

import requests
import urllib
import os

URL = 'http://1.1.1.3/ac_portal/login.php'

def login():
    # 读取文本数据
    f = open('data.txt','r')
    A = f.readlines()

    # 提交数据
    data1 = {
        'opr': 'pwdLogin',
        'userName': A[0].strip(),
        'pwd': A[1],
        'auth_tag': '',
        'rememberPwd': '1'
    }

    try:
        result = requests.post(URL,data=data1)
        if 'true' in result.text:
            print('successful!')
        else:
            print('failed!')
    except:
        print('no')

if __name__ == '__main__':
    while True:
        login()
        
