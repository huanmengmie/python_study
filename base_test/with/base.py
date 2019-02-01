# -*- coding: utf-8 -*-
"""
    1.使用__enter__() 和 __exit__()
    2.使用@contextManager
"""
import time

from decorator import contextmanager


class File(object):

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        try:
            self.f = open(self.file_name, self.mode)
        except FileNotFoundError as e:
            pass
        else:
            print("%s被打开了" % self.file_name)
            return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.f.close()
        except AttributeError as e:
            pass
        else:
            print("%s被关闭了" % self.file_name)


def test_method():
    with File('test.txt', 'r') as f:
        f.read()


@contextmanager
def open_file(file_name, mode):
    """
    yield方法之前的内容类似与__enter__()方法中
    yield方法之后的内容类似与__exit__()方法中
    :param file_name:
    :param mode:
    :return:
    """
    print("我要打开%s了" % file_name)
    f = open(file_name, mode)
    yield f
    f.close()
    print("我要关闭%s了" % file_name)


def test_context_manager():
    with open_file('test.txt', 'r') as f:
        f.read()
        time.sleep(2)


if __name__ == '__main__':
    test_method()
    print("*" * 20)
    test_context_manager()
