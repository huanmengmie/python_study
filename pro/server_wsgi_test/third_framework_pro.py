# -*- coding: utf-8 -*-
"""
    第三方框架
"""
import re
import os

from pro.server_wsgi_test.router import routers


def eval_path(path):
    for item in routers:
        if path == item[0]:
            return str(item[1])


def application(args, ret_header):
    """
    服务器调用第三方框架的入口
    :param args: 字典结构的参数
    :param ret_header:  生成的头部信息
    :return:
    """
    path = re.match(r'([/|\w]+)\.py', args.get("path"))
    location = args.get("location", "./template")

    req_file = eval_path(path.group(1))

    print("*" * 20, path, req_file, location + req_file)

    status = "200 OK"
    content = "请求资源不存在".encode('utf-8')

    if os.path.isfile(location + req_file):
        with open(location + req_file, 'rb') as file:
            content = file.read()
    else:
        status = "404 NOT FOUND"

    ret_header(status, [{"Content-Type", "text/html;charset=utf-8"}])
    return content
