import socket

# 创建socket
tcp_client = socket.socket()

# 链接服务器
server_addr = ("", 9528)
tcp_client.connect(server_addr)

# 获取要下载的文件
file_name = input("请输入要下载的文件名")

# 发送内容
tcp_client.send(file_name.encode("utf8"))

# 获取返回的数据
recv_file = tcp_client.recv(1024*1024)  # 1M

# 保存数据
if recv_file:
    with open("new_"+file_name, "wb") as f:
        f.write(recv_file)
    print("保存成功")

# 关闭链接
tcp_client.close()