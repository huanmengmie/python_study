# -*- coding: utf-8 -*-
"""
    Python支持多继承
    super().__init__(),根据mro继承链的顺序,一步步的向上继承,确保每个类只会被调用一次

    GrandSon init start
    Son1 init start
    Son2 init start
    Parent init start
    Parent init end
    Son2 init end
    Son1 init end
    GrandSon init end
    (<class '__main__.GrandSon'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)

"""


class Parent(object):
    def __init__(self, name, *args, **kwargs):
        print("Parent init start")
        self.name = name
        print("Parent init end")


class Son1(Parent):
    def __init__(self, name, sex, *args, **kwargs):
        print("Son1 init start")
        super().__init__(name, *args, **kwargs)
        self.sex = sex
        print("Son1 init end")


class Son2(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print("Son2 init start")
        super().__init__(name, *args, **kwargs)
        self.age = age
        print("Son2 init end")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, sex, *args, **kwargs):
        print("GrandSon init start")
        super().__init__(name,age, sex, *args, **kwargs)
        print("GrandSon init end")


if __name__ == '__main__':
    gs = GrandSon("lily", 18, "woman", "China")
    print(GrandSon.__mro__)
