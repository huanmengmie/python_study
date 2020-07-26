# -*- coding:UTF-8 -*-
""" 生产者消费者问题 """
from queue import Queue
from random import randint
from time import sleep

from pro.thread.my_thread import MyThread


def writeQ(queue):
    print('生产一个面包...')
    queue.put('xxx', 1)
    print('库存：', queue.qsize())


def readQ(queue):
    print('拿走一个面包...')
    queue.get(1)
    print('库存：', queue.qsize())


# 加工生产
def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


# 超市扫荡
def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(1, 3))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(4, 6)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('结束了')


if __name__ == '__main__':
    main()
