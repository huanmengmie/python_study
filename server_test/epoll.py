# -*- coding: utf-8 -*-
"""
    单进程单线程实现高并发,nginx和apache都是基于其实现
    epoll核心：
        1. 应用程序和内存之间 **共享部分内存**,降低资源拷贝时的消耗,
        2. 采用 **事件通知** 的方式监听socket列表
"""
import os
import re
import select
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
    tcp_server.bind(("", 9527))
    tcp_server.listen(128)

    # 创建一个epoll对象
    client_pool = select.epoll()

    # 将服务器套接字的fd放入epoll中,指定监听其数据输入
    client_pool.register(tcp_server.fileno(), select.EPOLLIN)

    client_socket_dict = dict()
    while True:
        fd_event_list = client_pool.poll()
        # [(fd, event),(fd, event)] fd文件描述符,event事件类型
        for fd, event in fd_event_list:
            if fd == tcp_server.fileno():
                new_socket, client_addr = tcp_server.accept()
                client_pool.register(new_socket.fileno(), select.EPOLLIN)
                client_socket_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recv_data = client_socket_dict.get(fd).recv(1024).decode('utf-8')
                if recv_data:
                    handle(client_socket_dict.get(fd), recv_data)
                else:  # 不再请求数据，从epoll中注销
                    client_socket_dict.get(fd).close()
                    client_pool.unregister(fd)
                    del client_socket_dict[fd]


if __name__ == '__main__':
    print("服务器启动成功")
    main()
