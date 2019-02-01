# -*- coding:UTF-8 -*-
import io
import sys
from urllib import request

import requests

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码


# 通过已有的cookie值模拟登录

# 使用urllib.request
def test1():
    cookie = r'p_h5_u=C998918D-911C-4251-B629-6407E0FA2FDE; UM_distinctid=1669a8768d5bdf-0807fe92676876-333b5602-1fa400-1669a8768d65dc; CNZZDATA1273363036=1707537421-1540190436-http%253A%252F%252Flocalhost%253A8888%252F%7C1545117941; admin_security_session="2|1:0|10:1545117946|22:admin_security_session|48:MjJhZmQyZDItMDI5Ni0xMWU5LWI1OTYtZjA3OTU5Njk5NzY0|1173c331d054a71563ab8cb28fa554aa29eb654a439616439e98f33658156b70"; admin_login_info="2|1:0|10:1545117946|16:admin_login_info|132:eyJsb2dpbl9pZCI6ICJhZG1pbiIsICJsb2dpbl9zZXNzaW9uIjogIjIyYWY5NjVhLTAyOTYtMTFlOS1iNTk2LWYwNzk1OTY5OTc2NCIsICJjb21wYW55X3R5cGUiOiAzMH0=|23c54232e8f25677c041b1dff3e2191751324e72d97f810590ffb15cb488a155"'
    url = r"http://localhost:8888/web/order_manage"
    req = request.Request(url)
    req.add_header("cookie", cookie)
    req.add_header("User-Agent",
                   r"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36")

    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))


# 使用requests库
def test2():
    existed_cookie = r'p_h5_u=C998918D-911C-4251-B629-6407E0FA2FDE; UM_distinctid=1669a8768d5bdf-0807fe92676876-333b5602-1fa400-1669a8768d65dc; CNZZDATA1273363036=1707537421-1540190436-http%253A%252F%252Flocalhost%253A8888%252F%7C1545117941; admin_security_session="2|1:0|10:1545117946|22:admin_security_session|48:MjJhZmQyZDItMDI5Ni0xMWU5LWI1OTYtZjA3OTU5Njk5NzY0|1173c331d054a71563ab8cb28fa554aa29eb654a439616439e98f33658156b70"; admin_login_info="2|1:0|10:1545117946|16:admin_login_info|132:eyJsb2dpbl9pZCI6ICJhZG1pbiIsICJsb2dpbl9zZXNzaW9uIjogIjIyYWY5NjVhLTAyOTYtMTFlOS1iNTk2LWYwNzk1OTY5OTc2NCIsICJjb21wYW55X3R5cGUiOiAzMH0=|23c54232e8f25677c041b1dff3e2191751324e72d97f810590ffb15cb488a155"'

    url = r"http://localhost:8888/web/order_manage"

    # 将cookie处理为字符串
    cookies = {}
    for line in existed_cookie.split(";"):
        key, value = line.split('=', 1)
        cookies[key] = value

    resp = requests.get(url, cookies=cookies)
    print(resp.__dict__)


if __name__ == "__main__":
    print("使用urllib.request")
    test1()
    print("使用requests")
    test2()
