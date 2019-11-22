# -*- coding:UTF-8 -*-
from functools import reduce


def test():
    try:
        result = 10/0
        print("出错了")
        return 1
    except ZeroDivisionError as e:
        return 0
        print(e)
        return 2
    finally:
        print("除数不能为0啊")
        return 3


def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


if __name__ == "__main__":
    main()
    # print(calc_time.py())
