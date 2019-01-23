# -*- coding: utf-8 -*-
"""
    Python支持多继承
    Class.__init__(),继承的时候使用这种方式,比较简单.
    但是会重复调用公共父类的的init()方法,可能会造成资源浪费

    GrandSon init start
    Son1 init start
    Parent init start
    Parent init end
    Son1 init end
    Son2 init start
    Parent init start
    Parent init end
    Son2 init end
    GrandSon init end
"""


class Parent(object):
    def __init__(self, name):
        print("Parent init start")
        self.name = name
        print("Parent init end")


class Son1(Parent):
    def __init__(self, name, sex):
        print("Son1 init start")
        Parent.__init__(self, name)
        self.sex = sex
        print("Son1 init end")


class Son2(Parent):
    def __init__(self, name, age):
        print("Son2 init start")
        Parent.__init__(self, name)
        self.age = age
        print("Son2 init end")


class GrandSon(Son1, Son2):
    def __init__(self, name, age, sex, region):
        print("GrandSon init start")
        Son1.__init__(self, name, sex)
        Son2.__init__(self, name, age)
        self.region = region
        print("GrandSon init end")


if __name__ == '__main__':
    gs = GrandSon("lily", 18, "woman", "China")
