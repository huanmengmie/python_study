# -*- coding: utf-8 -*-
"""
    gevent 基于 greenlet的协程实现
"""
import gevent


def task(n):
    for i in range(n):
        print("执行 %s => %d" % (gevent.getcurrent(), i))
        gevent.sleep(0.2)


def main():
    gevent.joinall([
        gevent.spawn(task, 5),
        gevent.spawn(task, 5),
        gevent.spawn(task, 5),
    ])


if __name__ == "__main__":
    main()
