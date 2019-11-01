# -*- coding:UTF-8 -*-
""" 文件操作 """
# 文件操作  mode: r 读，w 写，a 添加，(+ 读写，b 二进制访问) 有问题
# ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'b'

# 文件路径可为：1、相对路径（note.txt） 2、绝对路径 （D:/workspace/python_study/note.txt）
# aHandle = open('note.txt', 'a')   在已有内容上追加
# aHandle.writelines("\nPython代码添加内容到文件中")
# aHandle.close()
# print("书写完毕"

wHandle = open('./test.txt','w', encoding="utf8")  # 覆盖原有内容
wHandle.writelines("Python代码写内容到文件中")
wHandle.writelines("Python代码写内容到文件中")
wHandle.close()

# rHandle = open('D:/workspace/python_study/test.txt','r')
# for eachline in rHandle:
#     print(eachline,       # 加“，”可以抑制其自动生成换行符号
# rHandle.close()
# print
# print('读完了'


# ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'b'
# try:
#     # rw = open('../test.txt','b')
#     rw = open('../test.txt', 'a')
#     rw.writelines('\n读写模式下，写入新的内容')
#     for eachline in rw:
#         print(eachline
#     rw.close()
# except ValueError , e:
#     print('文件操作模式出错：',e
# except IOError , e:
#     print('操作文件出错：',e

