# -*- coding: utf-8 -*-
"""
    装饰器
        随着Python解释器执行到@decorator，就开始对方法进行装饰，不需要等到方法调用
"""
import time


# ------------------ 基础部分 ------------------
def count_time(func):
    print("开始进行方法装饰")

    def handle():
        start_time = time.time()
        func()
        end_time = time.time()
        print("\r\n%s方法耗时%s" % (func.__name__, end_time - start_time))

    return handle


# 语法糖 @count_time  等效于  test = count_time(test)
def test():
    for i in range(50):
        print(pow(i, 3), end="\t")


test = count_time(test)


@count_time
def test2():
    for i in range(50):
        print(pow(i, 3), end="\t")


# ------------------ 提高 ------------------

# 传递参数
def count_pro(func):
    def handle(*args, **kwargs):
        print("哈哈哈哈哈哈啊哈哈")
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print("\r\n%s方法耗时%s" % (func.__name__, end_time - start_time))
        return ret

    return handle


@count_pro
def print_info(num, *args, **kwargs):
    print("----", num)
    print("----", args)
    print("----", kwargs)


# 同一个函数上使用多个装饰器，最下方的最先被调用
def log(func):
    def handle(*args, **kwargs):
        print("%s方法开始了" % func.__name__)
        ret = func(*args, **kwargs)
        print("%s方法结束了" % func.__name__)
        return ret

    return handle


@count_pro
@log
def multi_decorator(*args, **kwargs):
    print("----", args)
    print("----", kwargs)


# ------------------ 带参数 ------------------
def admin_auth(permission):  # permission 传递的参数
    def wrapper(func):  # func 被装饰的方法
        def wrapped(*args, **kwargs):
            if permission == 10:
                print("青铜玩家")
            elif permission == 20:
                print("白银玩家")
            elif permission == 30:
                print("黄金玩家")
            return func(*args, **kwargs)
        return wrapped
    return wrapper


# 带参数的装饰器，先调用admin_auth方法，然后使用该方法的返回值装饰函数
@admin_auth(10)
def print1():
    print("啦啦啦啦")


@admin_auth(20)
def print2():
    print("啦啦啦啦")


@admin_auth(30)
def print3():
    print("啦啦啦啦")


if __name__ == '__main__':
    # test()
    # print("=" * 50)
    # test2()

    # print_info(12, 2, 35, 564, 34, name="张三", age=23)
    # print("=" * 50)
    # multi_decorator(12, 2, 35, 564, 34, name="张三", age=23)

    print1()
    print2()
    print3()
