# -*- coding: utf-8 -*-
"""
    基于tcp协议的聊天
"""

import socket

# 存储所有在线的客户端
import threading

client_list = []


# 获取在线成员
def get_members():
    members = map(lambda item: item.get("addr"), client_list)
    return list(members)


# 根据socket获取用户详细信息
def get_detail_info(client_socket):
    for i, item in enumerate(client_list):
        if item.get("socket") == client_socket:
            return i, item


# 群发消息
def send_mass_msg(msg):
    sockets = map(lambda item: item.get("socket"), client_list)
    for item in sockets:
        item.send(msg.encode("utf8"))
    else:
        print("发送完毕")


# 接收消息
def recv_msg(client_socket):
    # 获取详细信息
    index, client_info = get_detail_info(client_socket)
    name = client_info.get("addr")
    while True:
        content = client_socket.recv(1024).decode("utf8")
        if content == "exit()":
            client_socket.close()
            del client_list[index]
            break
        send_mass_msg("%s 说：%s" % (name, content))


def main():
    print("----------开启服务器---------")
    # 创建socket套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = ("", 9528)
    tcp_socket.bind(server_addr)

    # 将socket变为监听状态
    tcp_socket.listen(100)

    while True:
        client_socket, client_addr = tcp_socket.accept()
        client_list.append(dict(addr=client_addr, socket=client_socket))
        print("%s加入聊天室" % str(client_addr))
        send_mass_msg("欢迎%s加入聊天室\n" % str(client_addr))
        client_socket.send(("聊天室成员：\n %s" % get_members()).encode("utf8"))
        recv_thread = threading.Thread(target=recv_msg, args=(client_socket,))
        recv_thread.start()


if __name__ == "__main__":
    main()
