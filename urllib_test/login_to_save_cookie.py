# -*- coding:UTF-8 -*-
import http.cookiejar
import io
import sys
from urllib import request, parse

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


# 模拟登录后再携带得到的cookie访问
def test1():
    data = [
        ("username", 'admin'),
        ("password", 'a1234567'),
        ("action_type", "user_login"),
        ("company_type", 30)
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    login_url = r'http://localhost:8888/auth/login'

    login_data = parse.urlencode(data).encode('utf-8')
    print(login_data)

    # 构造登录请求
    req = request.Request(login_url, headers=headers, data=login_data)

    # 构造cookie
    cookie = http.cookiejar.CookieJar()

    # 由cookie构造opener
    opener = request.build_opener(request.HTTPCookieProcessor(cookie))

    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)

    print(resp.__dict__)

    for k, v in resp.getheaders():
        print('%s: %s' % (k, v))

    # 登录后才能访问的网页
    url = r"http://localhost:8888/web/order_manage"

    # 构造访问请求
    req2 = request.Request(url, headers=headers)

    resp2 = opener.open(req2)

    print(resp2.read().decode('utf-8'))


def test2():
    data = {
        "username": 'admin',
        "password": 'a1234567',
        "action_type": 'user_login',
        "company_type": 30
    }
    login_url = r'http://localhost:8888/auth/login'

    resp = requests.post(login_url, params=data)
    print(resp.cookies)

    url = r"http://localhost:8888/web/order_manage"
    resp2 = requests.get(url, cookies=resp.cookies)
    print(resp2.__dict__)
    print(resp2.text)


if __name__ == "__main__":
    # print("使用urllib.request")
    # test1()
    print("使用requests")
    test2()
