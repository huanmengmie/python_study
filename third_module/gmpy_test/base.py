# -*- coding:UTF-8 -*-
import gmpy2

def get_prec():
    prec = 3000000
    while True:
        gmpy2.get_context().precision = prec
        res = str(gmpy2.sqrt(2))
        print(prec, len(res))
        if len(res) >= 1000002:
            print(res[-1], len(res), prec)
            break
        else:
            prec += 1
    return prec


def calc():
    gmpy2.get_context().precision = 3321925
    res = str(gmpy2.sqrt(2))
    print(res[-1])   # => 9
    print(res)
##
# import sys
#
# n = 2
# s = 0
# res = []
# while True:
#     for si in range(9, -1, -1):
#         nx = n - ((2 * s * 10 + si) * si)
#         if nx >= 0:
#             s = s * 10 + si
#             n = nx * 100
#             # sys.stdout.write(str(si))
#             # sys.stdout.flush()
#             res.append(si)
#             print(si)
#             break


if __name__ == '__main__':
    calc()