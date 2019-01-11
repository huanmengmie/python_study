# -*- coding: utf-8 -*-
"""
    自定义迭代器
    实现 __init__  及  __next__ 方法
"""


class ClassMates(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def append(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        all_num = len(self.names)
        if all_num > self.current_num:
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    cls = ClassMates()
    cls.append("张三")
    cls.append("李四")
    cls.append("王五")
    cls.append("赵六")

    for item in cls:
        print(item)


if __name__ == "__main__":
    main()
