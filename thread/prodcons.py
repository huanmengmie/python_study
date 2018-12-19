# -*- coding:UTF-8 -*-
""" 生产者消费者问题 """
from random import randint
from time import sleep
from Queue import Queue
from my_thread import MyThread

def writeQ(quene):
    print "producing object for Q..."
    quene.put('xxx',1)
    print 'size now',quene.qsize()


def readQ(quene):
    print 'consuming object for Q...'
    quene.get(1)
    print 'size now',quene.qsize()


def writer(quene, loops):
    for i in range(loops):
        writeQ(quene)
        sleep(randint(1,3))


def reader(quene, loops):
    for i in range(loops):
        readQ(quene)
        sleep(randint(1,3))


funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(4,6)
    q = Queue(32)
    threads = []

    for i in nfuncs:
        t = MyThread(funcs[i],(q,nloops), funcs[i].__name__)
        threads.append(t)
    # threads.append(MyThread(funcs[0],(q,5), funcs[0].__name__))
    # threads.append(MyThread(funcs[1],(q,2), funcs[1].__name__))
    
    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print 'all done'

if __name__ == '__main__':
    main()