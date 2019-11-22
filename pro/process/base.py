# -*- coding:UTF-8 -*-
"""
    进程与进程池
"""

import time
from multiprocessing import Process, Pool
import os
import random


def run_proc(name):
    print("子进程 %s => %s" % (name, os.getpid()))
    print("哈哈")


def single_test():
    print("主进程 %s" % os.getpid())
    p = Process(target=run_proc, args=("calc_time.py",))
    print("子进程开始")
    p.start()
    p.join()
    print("子进程结束")


# pool calc_time.py
def long_time_task(task):
    print("任务%s=>%s开始了" % (task, os.getpid()))
    try:
        start = time.time()
        t = random.random() * 4
        time.sleep(t)
        end = time.time()
    except BaseException as e:
        print(e)
    print("任务%s=>%s结束了，耗时%0.2f" % (task, os.getpid(), (end - start)))


def pool_test():
    # 使用进程池创建任务
    print("主任务%s开始了" % os.getpid())
    p = Pool(5)
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))
    print("等待子任务执行")
    p.close()
    p.join()
    print("所有任务执行完毕")


if __name__ == "__main__":
    # single_test()
    pool_test()
