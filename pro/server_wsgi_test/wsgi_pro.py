# -*- coding: utf-8 -*-
"""
    WSGI：Web Server Gateway Interface
"""

import os
import re
import socket
import multiprocessing
import sys


# 加入模块搜索的路径，即临时环境变量
sys.path.append("server_wsgi_test")


class WSGIServer(object):
    with open("./config.json", "r") as f:
        text = f.read()
        content = eval(text)
    static_url = content.get("static_url")
    dynamic_url = content.get("dynamic_url")
    
    def __init__(self, app, port):
        self.app = app
        self.status = None
        self.headers = None
        self.tcp_server = socket.socket()
        # 设置可重用端口号
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server.bind(("", port))
        self.tcp_server.listen(128)

    def handle(self, client_socket):
        print("=" * 50)
        request = client_socket.recv(1024).decode('utf-8')
        print(request)
        request_list = request.splitlines()
        response_header = 'HTTP/1.1 200 OK\r\n'
        response_body = b''
        if request_list:
            ret = re.match(r'[^/]+(/[^ ]+)', request_list[0])
            if ret:
                req_info = ret.group(1).split(sep='?')
                req_file = req_info[0]
                if req_file.endswith(".py"):
                    args = dict(path=req_file, location=self.dynamic_url)
                    response_body = self.app(args, self.handle_header)
                    response_header = 'HTTP/1.1 %s\r\n' % self.status
                    for key, value in self.headers:
                        response_header += "%s:%s\r\n" % (key, value)

                else:
                    if os.path.isfile(self.static_url + req_file):
                        with open(self.static_url + req_file, 'rb') as file:
                            response_body = file.read()
                    else:
                        response_header = 'HTTP/1.1 404 NOT FOUND\r\n'
                        print(req_file + "找不到")

        response_header += 'Content-Length: %d\r\n' % len(response_body)
        response_header += '\r\n'
        response_info = response_header.encode('utf-8') + response_body
        client_socket.send(response_info)
        client_socket.close()
        
    def handle_header(self, status, headers):
        self.status = status
        self.headers = headers

    def start_server(self):
    
        while True:
            new_socket, client_addr = self.tcp_server.accept()
            p = multiprocessing.Process(target=self.handle, args=(new_socket,))
            p.start()
            # 多进程会自动复制fd(new_socket对应的文件描述符),因此需要全部关闭,才能确保发送成功
            new_socket.close()


def main():
    port = 9527
    module_name = "third_framework_pro"
    app_name = "application"
    # 从命令行读取运行环境信息
    args = sys.argv
    if len(args) == 3:
        port = int(args[1])
        module_info = args[2].split(".")
        module_name = module_info[0]
        app_name = module_info[1]
    # 动态加载模块，调用属性
    module = __import__(module_name)
    app = getattr(module, app_name)

    server = WSGIServer(app, port)
    server.start_server()


if __name__ == '__main__':
    print("服务器启动成功")
    print("你可以使用以下方式指定项目所使用的框架：python3 wsgi_pro.py port module.method")
    main()
