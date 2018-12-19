# -*- coding:UTF-8 -*-
import json

# 数组类型的元组转json
a = [(1,3,4),(2,5,8),(2,3,5)]
b = ('a','b','c')
print zip(b,a)

c = []
for item in a:
    c.append(dict(zip(b,item)))
    print dict(zip(b,item))

res = json.dumps(c)
print res