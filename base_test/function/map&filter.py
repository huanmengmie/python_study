# -*- coding: utf-8 -*-
""" map函数 filter函数 基本使用"""

my_list = []

for i in range(10):
    my_list.append(dict(id=i, name="张三"))


for i, j in my_list:
    print(i,j)


item = map(lambda item: item.get("id"), my_list)
print(list(item))


filter_item = filter(lambda item: item.get("id") == 2, my_list)
print(list(filter_item))
