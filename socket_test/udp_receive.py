import socket
# 创建socket套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定IP及端口号
local_addr = ("", 9527)
udp_socket.bind(local_addr)

# 获取数据
content, addr = udp_socket.recvfrom(1024)
print("%s: %s" % (str(addr), content.decode("utf8")))

# 发送数据
udp_socket.sendto("我收到了，告辞".encode("utf8"), addr)

# 关闭链接
udp_socket.close()