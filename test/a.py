# -*- coding:UTF-8 -*-

from b import B

class A(object):
    def a(self):
        b = B()
        b.b()
        print 'a'

if __name__ == '__main__':
    a = A()
    a.a()