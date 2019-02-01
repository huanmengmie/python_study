# -*- coding: utf-8 -*-
"""
    闭包
        方法调用时，会将外层方法的数据和内层方法的引用一同传递

        外层函数中的数据会保存在内存中，不会随方法的结束而被销毁

        内存函数修改外层函数的数据时需要使用nonlocal关键字

    闭包 与 对象
        闭包占用的空间较小
        对象的功能强大

"""


def base(k, b):
    """
    闭包，k 和 b 将会保存起来
    :param k:
    :param b:
    :return:
    """

    def inner_1(x):
        print(k * x + b)

    return inner_1


def test_1():
    t1 = base(3, 1)
    t1(0)
    t1(1)
    t1(2)
    print("=" * 20)
    t2 = base(3, 2)
    t2(0)
    t2(1)
    t2(2)


k = 0


def update():
    k = 1
    b = 2
    print("outer k:%d b:%d" % (k, b))

    def inner2():
        # 内层方法如果先使用外层数据，然后对数据进行修改，需要使用 nonlocal 关键字修饰
        nonlocal k
        print("inner k:%d" % k)
        k = 10
        print("inner k:%d " % k)
        # 若直接修改，则是在函数内部生成了一个同名的变量
        b = 1234
        print("inner b:%d " % b)

    print("final k:%d" % k)
    return inner2


def test_2():
    u = update()
    u()


def main():
    # test_1()
    test_2()


if __name__ == '__main__':
    main()
