# !/usr/bin/python
#coding=utf-8

import requests
import urllib
import os
import time
import configparser

URL = 'http://1.1.1.3/ac_portal/login.php'

config = configparser.ConfigParser()
path = 'data.ini'

def login():
    # 读取文本数据 
    config.read(path)
    username = config['select']['username']
    password = config['select']['password']

    # 提交数据
    data1 = {
        'opr': 'pwdLogin',
        'userName': username,
        'pwd': password,
        'auth_tag': '',
        'rememberPwd': '1'
    }

    try:
        result = requests.post(URL,data=data1)
        if 'true' in result.text:
            print('successful!')
        else:
            print('账号或密码有错!')
    except KeyboardInterrupt:
        print('停止程序')
        time.sleep(1)
        exit()

if __name__ == '__main__':
    while True:
        login()