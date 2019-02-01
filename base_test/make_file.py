# -*- coding:UTF-8 -*-
""" 创建新文件 """

import os
ls = os.linesep     # 获取换行符

fname = input("请输入文件名：\n")
mode = 'a'
# 判断文件是否存在
if os.path.exists(fname):
    print('INFO:%s文件已存在' % fname)
else:
    mode = 'w'
    print('请输入内容，输入“quit”退出')

# 向文件中写入内容
all = []
while True:
    content = input('> ')
    if content == 'quit':
        break
    else:
        all.append(content)
handler = open(fname,mode)
handler.writelines(['%s%s' % (x,ls) for x in all])
handler.close()
print('文件写入完毕')