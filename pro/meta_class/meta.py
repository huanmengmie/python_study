# -*- coding: utf-8 -*-
"""
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
"""


# 简单版本
class Upper(type):
    def __new__(cls, name, parent, attrs):
        print(cls)
        print(name)
        print(parent)
        print(attrs)
        return type(name, parent, attrs)


class Test(object, metaclass=Upper):  # 指定创建Foo的type为SingletonType
    a = "sdkfj"
    b = "234"


t = Test()


# 升级版本
class SingletonType(type):
    def __init__(cls, *args, **kwargs):
        print("meta init")
        super(SingletonType, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):  # 这里的cls，即Foo类
        print('cls', cls)
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)  # Foo.__init__(obj)
        return obj


class Foo(object, metaclass=SingletonType):  # 指定创建Foo的type为SingletonType
    def __init__(self, name):
        print("foo init")
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("foo new")
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print("call方法被调用了")


obj = Foo('xx')
obj()
print(Foo.__mro__)
