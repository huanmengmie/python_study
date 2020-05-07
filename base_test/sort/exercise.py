# -*- coding:utf-8 -*-
import time


def count_time(func):
    print("开始进行方法装饰")

    def handle(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("\r\n%s方法耗时%s" % (func.__name__, end_time - start_time))
        return res

    return handle


class MinStack:
    """设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
        使用一个备胎栈，比当前最小值的元素入栈
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min_data) == 0 or self.get_min() >= x:
            self.min_data.append(x)

    def pop(self) -> None:
        d = self.data.pop()
        if d == self.get_min():
            self.min_data.pop()

    def top(self) -> int:
        return self.data[len(self.data) - 1]

    def get_min(self) -> int:
        return self.min_data[len(self.min_data) - 1]


class GreatestCommonDivisor:
    """
        求最大公约数
        1、辗转相除法（欧几里得算法）基于一个定理。两个正整数a和b(a>b),它们的最大公约数等于a和b的余数c 与b之间的最大公约数
            时间复杂度：近似为O(log(max(a, b)))     问题：当a和b过大时，取模运算性能变差
        2、更相减损术  两个正整数a和b(a>b),它们的最大公约数等于a和b的差c 与b之间的最大公约数
            时间复杂度：最差O(max(a,b))      问题：当a和b相差太大，运算次数过多
        3、辗转相除法与更相减损术结合  时间复杂度O(log(max(a,b)))
    """

    @staticmethod
    @count_time
    def divisor(a, b):
        """辗转相除法（欧几里得算法）"""
        if a < b:
            a, b = b, a
        while True:
            c = a % b
            if c != 0:
                a, b = b, c
            else:
                break
        return b

    def divisor2(self, a, b):
        """ 辗转相除法（欧几里得算法）基于一个定理。两个正整数a和b(a>b),它们的最大公约数等于a和b的余数c 与b之间的最大公约数 """
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        else:
            return self.divisor2(b, a % b)

    def divisor3(self, a, b):
        """ 更相减损术  两个正整数a和b(a>b),它们的最大公约数等于a和b的差c 与b之间的最大公约数 """
        if a < b:
            a, b = b, a
        if a - b == 0:
            return b
        else:
            return self.divisor3(b, a - b)

    def divisor4(self, a, b):
        """ 前两者结合 """
        if a == b:
            return a
        # 两者都为偶数 gcd(a,b) = 2 * gcd(a/2, b/2) = gcd(a>>1, b>>1) << 1
        if a & 1 == 0 and b & 1 == 0:
            return self.divisor4(a >> 1, b >> 1) << 1
        # 其中一个（如a）为偶数时 gcd(a, b) = gcd(a/2, b) = gcd(a>>1, b)
        elif a & 1 == 0 and b & 1 != 0:
            return self.divisor4(a >> 1, b)
        elif a & 1 != 0 and b & 1 == 0:
            return self.divisor4(a, b >> 1)
        # 当两者都为奇数时， gcd(a,b) = gcd(b, a-b)
        elif a & 1 != 0 and b & 1 != 0:
            if a < b:
                a, b = b, a
            return self.divisor4(b, a - b)


def is_power_of_2(num):
    """ 判断一个数是否为2的n次幂 """
    return num & (num - 1) == 0


def second_max_num(nums):
    """ 一个数组的第一和第二最大值 """
    if len(nums) < 2:
        return
    m1, m2 = nums[0], nums[1]
    if m2 > m1:
        m1, m2 = m2, m1
    for i in nums[2:]:
        if i >= m1:  # 比前两个都大
            m2 = m1
            m1 = i
        elif i > m2:
            m2 = i
    print(m1, m2)


def handle_equation(x):
    return pow(x, 8) + 8 * (pow(x, 4)) - 8 * (pow(x, 5)) - 1



if __name__ == '__main__':
    # d = GreatestCommonDivisor()
    # print(d.divisor(24, 18))
    # print(d.divisor2(24, 18))
    # print(d.divisor3(100, 80))
    # print(d.divisor4(100, 80))
    # second_max_num([23, 96, 56, 23, 34, 4, 5])

    print(handle_equation(259, 3))