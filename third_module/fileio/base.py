# -*- coding:UTF-8 -*-
""" 文件操作 """
# 文件操作  mode: r 读，w 写，a 添加，(+ 读写，b 二进制访问) 有问题
# ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'b'
import json
import shutil
# 文件路径可为：1、相对路径（note.txt） 2、绝对路径 （D:/workspace/python_study/note.txt）
# aHandle = open('note.txt', 'a',encoding="utf8")  # 在已有内容上追加
# aHandle.writelines("\nPython代码添加内容到文件中")
# aHandle.close()
# print("书写完毕")

# wHandle = open('../calc_time.py.txt','w')  # 覆盖原有内容
# wHandle.writelines("Python代码写内容到文件中")
# wHandle.close()

rHandle = open('D:/workspace/python_study/calc_time.py.txt','r',encoding="utf8")
for line in rHandle.readlines():
    print(line.strip()),      # 加“，”可以抑制其自动生成换行符号
print(rHandle.read())
rHandle.close()
print('读完了')

# rHandle = open('D:/workspace/python_study/calc_time.py.txt','r')
# longest = max(len(x.strip()) for x in rHandle)
# print('longest:',longest

# aHandle = open('../note.txt', 'r+')  # 在已有内容上追加
# aHandle.writelines("\nPython代码添加内容到文件中")
# for eachline in aHandle:
#     print(eachline
# aHandle.close()
# print("书写完毕"

# ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not 'b'
# try:
#     # rw = open('../calc_time.py.txt','b')
#     rw = open('../calc_time.py.txt', 'a')
#     rw.writelines('\n读写模式下，写入新的内容')
#     for eachline in rw:
#         print(eachline
#     rw.close()
# except ValueError , e:
#     print('文件操作模式出错：',e
# except IOError , e:
#     print('操作文件出错：',e


from operator import add, sub
nums = [3, 5]
n = add(*nums)
m = sub(*nums)
print(n,m)


def bar():
    foo()
    print('in bar')

def foo():
    print('in foo')

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
