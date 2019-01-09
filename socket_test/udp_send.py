import socket

# 创建socket套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
udp_socket.sendto('哈哈哈'.encode('utf8'), ('', 9527))

# 获得接收方的反馈
content, addr = udp_socket.recvfrom(1024)
print("%s: %s" % (str(addr), content.decode("utf8")))

# 关闭链接
udp_socket.close()
