# -*- coding: utf-8 -*-
"""
    第三方框架
"""


def hello():
    return "欢迎页面..."


def index():
    return "主页面..."


def application(args, ret_header):
    """
    服务器调用第三方框架的入口
    :param args: 字典结构的参数
    :param ret_header:  生成的头部信息
    :return:
    """
    path = args.get("path")
    print(path)
    status = "200 OK"
    content = "请求资源不存在"

    if path == "/hello.py":
        content = hello()

    elif path == "/index.py":
        content = index()

    else:
        status = "404 NOT FOUND"

    ret_header(status, [{"Content-Type", "text/html;charset=utf-8"}])
    return content.encode('utf-8')
