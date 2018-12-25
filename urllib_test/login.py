# -*- coding:UTF-8 -*-
import http.cookiejar
from urllib import request, parse


# 通过已有的cookie值模拟登录
def test1(cookie, url, filename):
    req = request.Request(url)
    req.add_header("cookie", cookie)
    req.add_header("User-Agent",
                   r"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36")

    with request.urlopen(req) as resp:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(resp.read().decode('utf-8'))
            print(resp.read().decode('utf-8'))


# 通过用户名密码登录
def test2():
    # name = input("请输入账号:")
    # password = input("请输入密码:")
    data = [
        ("username", 'admin'),
        ("password", 'a1234567'),
        ("action_type", "user_login"),
        ("company_type", 30)
    ]

    # req = request.Request('http://localhost:8888/auth/login')
    # req.add_header('Origin', 'http://localhost:8888')
    # req.add_header('User-Agent',
    #                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')
    # req.add_header('Referer',
    #                'http://localhost:8888/auth/login')
    headers = {
        'Origin': 'http://localhost:8888',
        'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Referer': 'http://localhost:8888/auth/login'
    }
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

    for k, v in resp.getheaders():
        print('%s: %s' % (k, v))

    # # 登录后才能访问的网页
    # url = r"http://10.0.27.7:8888/web/order_manage"
    #
    # # 构造访问请求
    # req = request.Request(url, headers=headers)
    #
    # resp = opener.open(req)

    # print(resp.read().decode('utf-8'))


if __name__ == "__main__":
    # cookie = r'p_h5_u=C998918D-911C-4251-B629-6407E0FA2FDE; UM_distinctid=1669a8768d5bdf-0807fe92676876-333b5602-1fa400-1669a8768d65dc; CNZZDATA1273363036=1707537421-1540190436-http%253A%252F%252F10.0.27.7%253A8888%252F%7C1545117941; admin_security_session="2|1:0|10:1545117946|22:admin_security_session|48:MjJhZmQyZDItMDI5Ni0xMWU5LWI1OTYtZjA3OTU5Njk5NzY0|1173c331d054a71563ab8cb28fa554aa29eb654a439616439e98f33658156b70"; admin_login_info="2|1:0|10:1545117946|16:admin_login_info|132:eyJsb2dpbl9pZCI6ICJhZG1pbiIsICJsb2dpbl9zZXNzaW9uIjogIjIyYWY5NjVhLTAyOTYtMTFlOS1iNTk2LWYwNzk1OTY5OTc2NCIsICJjb21wYW55X3R5cGUiOiAzMH0=|23c54232e8f25677c041b1dff3e2191751324e72d97f810590ffb15cb488a155"'
    # url = r"http://10.0.27.7:8888/web/order_manage"
    # filename = r"D:/test.html"
    # test1(cookie, url, filename)
    test2()
