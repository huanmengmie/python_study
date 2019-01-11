# -*- coding: utf-8 -*-
"""
    生成器
"""


# 使用列表解析（）
def test1():
    a = [x for x in range(10)]
    print("a的类型：",type(a))

    b = (x for x in range(10))
    print("b的类型：",type(b))


# 使用yield关键字
def test2(times):
    a, b = 0, 1
    cur_num = 0
    while cur_num <= times:
        yield a
        a, b = b, a+b
        cur_num += 1


# 使用send传值
def test3(times):
    a, b = 0, 1
    cur_num = 0
    while cur_num <= times:
        field = yield a
        print("从外部传进来的值：", field)
        a, b = b, a+b
        cur_num += 1


if __name__ == "__main__":
    test1()

    print("*"*30)

    gen = test2(10)
    # list()内部调用生成器的next()方法，将值保存在集合中
    print(type(gen), list(gen))

    print("*" * 30)

    gen2 = test3(10)
    # 调用next() 方法可以中生成器中取值
    print(next(gen2))
    gen2.send("哈哈哈")
    # list()内部调用生成器的next()方法，将值保存在集合中
    print(type(gen2), list(gen2))
