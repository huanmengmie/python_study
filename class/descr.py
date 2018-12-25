# -*- coding:UTF-8 -*-
""" 使用文件来存储属性 """

import os , pickle

class Filedescr(object):
    saved = []

    def __init__(self, name = None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in Filedescr.saved:
            raise AttributeError('%r userd before assignmeng ' % self.name)

        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError,AttributeError,ImportError,IndexError) as e:
            raise AttributeError('could not read %r:%s' % self.name)

    def __set__(self, obj, value):
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(value, f)
                Filedescr.saved.append(self.name)
            except(TypeError,pickle.PicklingError) as e:
                raise AttributeError('could not pickle %r' % self.name)
        finally:
            f.close()

    def __delete__(self, instance):
        try:
            os.unlink(self.name)
            Filedescr.saved.remove(self.name)
        except(OSError, ValueError) as e:
            pass


class MyFileVarClass(object):
    foo = Filedescr('foo')
    bar = Filedescr('bar')

fvc = MyFileVarClass()
print (fvc.foo)