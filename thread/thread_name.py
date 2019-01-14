# -*- coding:UTF-8 -*-
"""
设置线程名称
"""
import threading


def loop():
    print("线程 %s 执行中..." % threading.current_thread().name)

    n = 0
    while n < 5:
        print("thread %s => %s" % (threading.current_thread().name, n))
        n += 1
    print("loop方法中=》当前线程:", threading.enumerate())
    print("线程 %s 执行结束..." % threading.current_thread().name)


def main():
    print("线程 %s 执行中..." % threading.current_thread().name)
    t = threading.Thread(target=loop, name="LoopThread")
    t.start()
    print("main方法=》当前线程:", threading.enumerate())
    t.join()
    print("线程 %s 执行结束..." % threading.current_thread().name)


if __name__ == "__main__":
    main()
