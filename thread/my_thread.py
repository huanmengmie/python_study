# -*- coding:UTF-8 -*-
""" threading.Thread类的派生子类 """
import threading
from time import ctime


def loop():
    print("threading %s running..." % threading.current_thread().name)

    n = 0
    while n < 5:
        print("thread %s => %s" % (threading.current_thread().name, n))
        n += 1
    print("threading %s ended..." % threading.current_thread().name)


def main():
    print("threading %s running..." % threading.current_thread().name)
    t = threading.Thread(target=loop, name="LoopThread")
    t.start()
    t.join()
    print("threading %s ended..." % threading.current_thread().name)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.func(*self.args)
        print(self.name, 'finished at ', ctime())


if __name__ == "__main__":
    main()
