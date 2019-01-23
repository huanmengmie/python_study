# -*- coding: utf-8 -*-
"""
    Python支持多继承
    super(Parent, self).__init__(),根据mro继承链的顺序,直接找下一个类

    GrandSon init start
    Parent init start
    Parent init end
    GrandSon init end
    (<class '__main__.GrandSon'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)

"""


class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("Parent init start")
        super().__init__()
        self.name = name
        print("Parent init end")


class Son1(Parent):
    def __init__(self, name, sex, *args, **kwargs):
        print("Son1 init start")
        self.sex = sex
        super(Parent, self).__init__(name, *args, **kwargs)
        print("Son1 init end")


class Son2(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son2 init start")
        self.age = age
        super(Parent, self).__init__(name, *args, **kwargs)
        print("Son2 init end")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, sex):
        print("GrandSon init start")
        super(Son2, self).__init__(name, age, sex)
        print("GrandSon init end")


if __name__ == '__main__':
    gs = GrandSon("lily", 18, "woman")
    print(GrandSon.__mro__)
