# -*- coding:UTF-8 -*-
from urllib.request import urlretrieve

# f = urlopen('http://fanyi.baidu.com/?aldtype=16047#en/zh/retrieve')
# lines = f.readlines()
# f.close()
#
# for eachline in lines:
#     print(eachline)
# print('读完了')

f = urlretrieve('http://www.null.com/home/index.html',r'D:/index.html')
print('读完了',f[0])