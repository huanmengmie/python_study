# -*- coding: utf-8 -*-
"""
单行输出进度
"""
import time


if __name__ == "__main__":
    num = 100
    complete_num = 0
    for item in range(100):
        complete_num += 1
        time.sleep(0.1)
        print("\r已完成%.2f%%" % (complete_num * 100 / num), end="")
