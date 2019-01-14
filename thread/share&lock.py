# -*- coding: utf-8 -*-
"""
    多线程共享全局变量以及锁的使用
"""
import threading

# 创建锁对象
lock = threading.Lock()

# 共享的全局变量
num = 0
num2 = 0

loop = 1000000


def test1():
    global num
    for i in range(loop):
        num += 1
    print("test1 num => %s" % num)


def test2():
    global num
    for i in range(loop):
        num += 1
    print("test2 num => %s" % num)


def test3():
    global num2
    for i in range(loop):
        lock.acquire()
        num2 += 1
        lock.release()
    print("test3 num => %s" % num2)


def test4():
    global num2
    for i in range(loop):
        lock.acquire()
        num2 += 1
        lock.release()
    print("test2 num => %s" % num2)


def main():
    print("没有加锁")
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main num => %s" % num)


def main2():
    print("加锁了")
    t1 = threading.Thread(target=test3)
    t2 = threading.Thread(target=test4)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("main num => %s" % num2)


if __name__ == "__main__":
    main()
    print("="*20)
    main2()
