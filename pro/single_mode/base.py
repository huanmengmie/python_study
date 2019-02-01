# -*- coding: utf-8 -*-
"""
    单例模式

   - 使用模块

　　- 使用__new__

　　- 使用装饰器

　　- 使用元类（metaclass）
"""

# 从其它模块导入
import threading

from pro.single_mode.single import test1

print(test1)


# 使用__new__
class Singleton(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__init__(cls)
            # cls.instance = object.__new__(cls)
            return cls.instance


# 使用装饰器
def single(cls):
    single_class = dict()

    def handle(*args, **kwargs):
        if cls not in single_class:
            single_class[cls] = cls(*args, **kwargs)
        return single_class.get(cls)

    return handle


@single
class Test(object):
    pass


# 使用元类
class SingletonType(type):
    _instance_lock = threading.Lock()

    # 添加类属性
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, name):
        self.name = name


obj1 = Foo('name')
obj2 = Foo('name')
print(obj1, obj2)

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(id(s1), id(s2), s1 is s2)

    t1 = Test()
    t2 = Test()
    print(id(t1), id(t2), t1 is t2)

    f1 = Foo("aa")
    f2 = Foo("aa")
    print(id(f1), id(f2), f1 is f2)

    print(Foo.__dict__)
