# -*- coding: utf-8 -*-
"""
    多进程版本
"""
import os
import re
import socket
import multiprocessing
import time


def handle(client_socket):
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
            time.sleep(1)
            if os.path.isfile('./pages' + req_file):
                with open('./pages' + req_file, 'rb') as file:
                    response_body = file.read()
            else:
                response_header = 'HTTP/1.1 404 NOT FOUND\r\n'
                print(req_file + "找不到")

    response_header += 'Content-Length: %d\r\n' % len(response_body)
    response_header += '\r\n'
    response_info = response_header.encode('utf-8') + response_body
    client_socket.send(response_info)
    client_socket.close()


def main():
    tcp_server = socket.socket()
    # 设置可重用端口号
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("", 9527))
    tcp_server.listen(128)

    while True:
        new_socket, client_addr = tcp_server.accept()
        p = multiprocessing.Process(target=handle, args=(new_socket,))
        p.start()
        # 多进程会自动复制fd(new_socket对应的文件描述符),因此需要全部关闭,才能确保发送成功
        new_socket.close()


if __name__ == '__main__':
    print("服务器启动成功")
    main()
