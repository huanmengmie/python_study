# -*- coding:UTF-8 -*-
""" class 类声明 """

# Python中没有缩进的代码行为最高级别的Python语句，在模块导入时就会被执行
print "我被其它模块引入了"

class Person(object):
    """ 第一个Python类 """
    age = 18     # 类属性

    def __init__(self, name='hq'):    # python 中用下划线开头结尾的（_XX_）都是特殊方法
        """ 类被实例化时第一个被调用的方法 """
        self.name = name
        print name, "加入了"

    def showName(self):      # self 是类实例自身的引用，相当于其他语言中的this
        print self.name

    def showAge(self):
        print self.name,'说我%d了'% self.age

    def setAge(self, x):
        self.age = x


def test():
    print '直接运行时执行测试方法'


if __name__ == '__main__':
    test()
    print '模块直接执行',__name__
else:
    print '模块被导入',__name__


def hehe():
    print "类外声明的方法"

