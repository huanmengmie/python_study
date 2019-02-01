# -*- coding: utf-8 -*-
"""
    元类
        使用type创建类
"""


class Test(object):
    a = "哈哈"
    b = "2"

    def print_a(self):
        print(self.a)

    @classmethod
    def print_b(cls):
        print(cls.b)

    @staticmethod
    def print_ha():
        print("ha")


help(Test)
print("-" * 20)


def print_a(self):
    print(self.a)


@classmethod
def print_b(cls):
    print(cls.b)


@staticmethod
def print_ha():
    print("ha")


Test1 = type("Test1", (), {"a": "哈哈", "b": 2, "print_a": print_a, "print_b": print_b, "print_ha": print_ha})
help(Test1)
print("*" * 50)
