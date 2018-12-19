# -*- coding:UTF-8 -*-
""" 函数 """

# from time import ctime,sleep
#
#
# def tsfunc(func):
#     def wrappedFunc():
#         print '[%s] %s() called ' % (ctime(),func.__name__)
#         return func()
#     return wrappedFunc
#
# @tsfunc
# def foo():
#     pass
#
# def test():
#     pass
#
#
# print foo
# print test
#
#
# foo()
#
# sleep(2)
#
# for i in range(3):
#     sleep(1)
#     foo()
# else:
#     print '打完了'

# 闭包
# def counter(start_at = 0):
#     count = [start_at]
#     def incr():
#         count[0] += 1
#         return count[0]
#     return incr
#
# count = counter(5)
# print count()
# print count()

j, k = 1, 2
def proc1():
    j,k = 3,4
    print 'p1:j == %d and k == %d' % (j,k)        # 3,4
    k = 5

def proc2():
    j = 6
    proc1()                                        # 3，4
    print 'p2:j == %d and k == %d' % (j, k)        # 6,7


k = 7
proc1()                                             # 3,4
print 'a1:j == %d and k == %d' % (j,k)             # 1,7

j = 8
proc2()                                     # 3,4      3,5
print 'a2:j == %d and k == %d' % (j,k)             #8,7

rows = [1,2,3,17]
def cols():
    yield 56
    yield 2
    yield 1

for pair in ((i,j) for i in rows for j in cols()):
    print pair
