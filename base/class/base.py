# -*- coding:UTF-8 -*-
""" 类 """


class ClassTest(object):
    num = 100


print(ClassTest.num)  # 100
ClassTest.num += 3

c = ClassTest()
print(c.num)  # 103
c.num += 5  # 执行 += 操作时, c.num的引用指向了另一块内存区域,对其进行修改,并不会影响类属性
print(c.num)  # 108

print(ClassTest.num)  # 103

c2 = ClassTest()
print(c2.num)  # 103

print(ClassTest.__dict__)
