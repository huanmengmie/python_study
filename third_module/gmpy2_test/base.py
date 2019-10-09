# -*- coding:UTF-8 -*-
import gmpy2
import time
import numpy


def get_prec():
    prec = 3000000
    while True:
        gmpy2.get_context().precision = prec
        res = str(gmpy2.sqrt(2))
        print(prec)
        if len(res) >= 1000002:
            print(res[-1], len(res), prec)
            break
        else:
            prec += 1
    return prec


def calc():
    # gmpy2.get_context().precision = 3321925
    start = time.time()
    for i in range(3321925, 3321930):
        t = time.time()
        gmpy2.get_context().precision = i
        res = str(gmpy2.sqrt(2))
        print("精度设置为{}, 运算长度为{}, 第一百万位数字是{}, 本次用时{}".format(i, len(res), res[-1], time.time() - t))
    end = time.time()
    print("总用时{}秒".format(end - start))

if __name__ == '__main__':
    calc()

