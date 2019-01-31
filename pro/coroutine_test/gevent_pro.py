# -*- coding: utf-8 -*-
"""
    gevent打补丁
"""
import gevent
from gevent import monkey
import time


# 将所有可能造成延时阻塞的方法改为调用gevent中提供的对象
monkey.patch_all()


def task(n):
    for i in range(n):
        print("执行 %s => %d" % (gevent.getcurrent(), i))
        time.sleep(0.2)


def main():
    start = time.time()
    gevent.joinall([
        gevent.spawn(task, 5),
        gevent.spawn(task, 5),
        gevent.spawn(task, 5),
    ])
    end = time.time()
    print(end-start)


if __name__ == "__main__":
    main()
