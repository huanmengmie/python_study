# -*- coding: utf-8 -*-
import socket
import threading


# 发送消息
def send_msg(socket):
    while True:
        content = input("请输入要发送的内容:\n")
        socket.send(content.encode("utf8"))
        if content == "exit()":
            socket.close()
            break


# 接收消息
def recv_msg(socket):
    while True:
        content = socket.recv(1024)
        if content:
            print(content.decode("utf8"))


def main():
    print("----开始聊天了-----")
    print("                                       ps:输入exit()退出聊天")
    client_socket = socket.socket()
    # 连接服务器
    server_addr = ("", 9528)
    client_socket.connect(server_addr)
    send = threading.Thread(target=send_msg, args=(client_socket,))
    send.start()
    recv = threading.Thread(target=recv_msg, args=(client_socket,))
    recv.start()


if __name__ == "__main__":
    main()
