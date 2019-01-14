# -*- coding: utf-8 -*-
"""
    协程：基础实现
"""


def task1():
    while True:
        print("任务1： hello")
        yield


def task2():
    while True:
        print("任务2： hi")
        yield


def main(num):
    i = 0
    t1 = task1()
    t2 = task2()
    while i < num:
        next(t1)
        next(t2)
        i += 1


if __name__ == "__main__":
    main(100)
