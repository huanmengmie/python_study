# -*- coding:UTF-8 -*-
""" 类 """

class ClassTest(object):
    num = 100


print ClassTest.num         # 100
ClassTest.num += 3


c = ClassTest()
print c.num                 # 101
c.num += 5
print c.num                 # 102

print ClassTest.num         # 102


c2 = ClassTest()
print c2.num

print ClassTest.__dict__
