# -*- coding: utf-8 -*-
"""
    使用@property装饰器
"""


class People(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        if self.__name:
            return self.__name+"哈哈"
        else:
            print("木有名字")

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print("类型错误")

    @name.deleter
    def name(self):
        del self.__name
        print("名字被删除了")



if __name__ == '__main__':
    p = People("张三")
    print(p.name)
    p.name = "李四"
    print(p.name)
    p.name = 23434
    print(p.name)
    del p.name
    # print(p.name)  # 调用报错,没有name属性
