# -*- coding: utf-8 -*-
"""
    长连接,非阻塞实现并发
    轮询列表
"""
import os
import re
import socket


def handle(client_socket, request):
    print("=" * 50)
    request_list = request.splitlines()
    response_header = 'HTTP/1.1 200 OK\r\n'
    response_body = b''
    if request_list:
        ret = re.match(r'[^/]+(/[^ ]+)', request_list[0])
        if ret:
            req_info = ret.group(1).split(sep='?')
            req_file = req_info[0]
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


def main():
    tcp_server = socket.socket()
    # 设置可重用端口号
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设置socket为非阻塞
    tcp_server.setblocking(False)
    tcp_server.bind(("", 9526))
    tcp_server.listen(128)

    client_socket_list = []
    while True:
        try:
            new_socket, client_addr = tcp_server.accept()
        except BlockingIOError as e:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

            for cli_socket in client_socket_list:
                try:
                    recv_data = cli_socket.recv(1024).decode('utf-8')
                except BlockingIOError as ret:
                    pass
                else:
                    if recv_data:
                        handle(cli_socket, recv_data)
                    else:
                        client_socket_list.remove(cli_socket)


if __name__ == '__main__':
    print("服务器启动成功")
    main()
