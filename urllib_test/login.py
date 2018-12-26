# -*- coding:UTF-8 -*-
import http.cookiejar
import io
import sys
from urllib import request, parse

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码



# 使用session保持会话状态
def test3():
    data = [
        ("username", 'admin'),
        ("password", 'a1234567'),
        ("action_type", "user_login"),
        ("company_type", 30)
    ]

    login_url = 'http://10.0.27.7:8888/auth/login'

    # 构造session
    session = requests.Session()

    # 发送登录请求，此后这个opener就携带了session，以证明自己登录过
    resp = session.post(login_url, data)

    print(resp.__dict__)

    # 登录后才能访问的网页
    url = "http://10.0.27.7:8888/web/order_manage"

    resp2 = session.get(url)

    print(resp2.content.decode('utf-8'))


if __name__ == "__main__":
    # cookie = r'p_h5_u=C998918D-911C-4251-B629-6407E0FA2FDE; UM_distinctid=1669a8768d5bdf-0807fe92676876-333b5602-1fa400-1669a8768d65dc; CNZZDATA1273363036=1707537421-1540190436-http%253A%252F%252F10.0.27.7%253A8888%252F%7C1545117941; admin_security_session="2|1:0|10:1545117946|22:admin_security_session|48:MjJhZmQyZDItMDI5Ni0xMWU5LWI1OTYtZjA3OTU5Njk5NzY0|1173c331d054a71563ab8cb28fa554aa29eb654a439616439e98f33658156b70"; admin_login_info="2|1:0|10:1545117946|16:admin_login_info|132:eyJsb2dpbl9pZCI6ICJhZG1pbiIsICJsb2dpbl9zZXNzaW9uIjogIjIyYWY5NjVhLTAyOTYtMTFlOS1iNTk2LWYwNzk1OTY5OTc2NCIsICJjb21wYW55X3R5cGUiOiAzMH0=|23c54232e8f25677c041b1dff3e2191751324e72d97f810590ffb15cb488a155"'
    # url = r"http://10.0.27.7:8888/web/order_manage"
    # filename = r"D:/test.html"
    # test1(cookie, url, filename)

    # test2()

    test3()
