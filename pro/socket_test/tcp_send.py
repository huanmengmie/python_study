import socket

# 创建socket
tcp_client = socket.socket()

# 链接服务器
server_addr = ("", 9528)
tcp_client.connect(server_addr)

# 发送内容
tcp_client.send("我是tcp链接".encode("utf8"))

# 关闭链接
tcp_client.close()