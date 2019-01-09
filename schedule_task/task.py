# -*- coding:UTF-8 -*-

"""
定时任务
    每5秒调用一次hello()方法
"""
from twisted.internet import reactor, task
from twisted.python import log


def hello():
    print('hello')


def err_callback(e, t):
    log.err(e)
    reactor.callLater(5, t)


def task_test():
    ts = task.LoopingCall(hello)
    d = ts.start(5, True)
    d.addErrback(err_callback, task_test)


if __name__ == '__main__':
    task_test()
    reactor.run()
