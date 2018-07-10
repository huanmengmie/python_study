# -*- coding:UTF-8 -*-
"""函数操作，常用内建函数"""

import my_class


tom = my_class.Person('tom')
tom.showAge()
# dir()显示对象属性
print 'dir()方法',dir(tom)
# help()显示对象的文档字符串，API文档。在终端使用
# int() 将对象转换为整型
print 'int和str比较', 16 == '16'
print 'int()方法',16 == int('16')
# str() 将对象转换为字符串
print 'str()方法','18' == str(18)
# len() 对象长度
print 'len()方法',len('asdfgd')
# open() 文件读写操作
# range(start,stop,step) 返回一个整型列表
print 'range()方法',range(1,6,2)
# type() 返回对象类型
print 'type()方法',type(22),type('sdf')
# raw_input() 从控制台输入信息，默认为String类型
str = raw_input('随便写点什么：')
print '你输入的是',str


def add(x, y):
    """执行x+y操作，并将值返回"""
    return x + y


print add(3, 5)


def factorial(debug=True):
    """x的y次方"""
    if debug :
        print 'debug模式'
    else:
        print '生产模式'


factorial()
factorial(False)


# 标准类型的内建函数
# cmp(3,5)                 # 对象比较   对数值和字符串比较
# repr([1,3,'sd'])  和  ``       # 返回对象的字符串表示,大部分可以用eval()函数得到其原来的对象，不建议使用 ``
# str([1,2,'sdf'])        # 返回对象的字符串表示，很少支持eval()函数
# type(1)                  # 返回数据类型
# isinstance(1,(int,float,complex,long))

# >>> type(1)
# <type 'int'>
# >>> type(1).__name__
# 'int'

# >>> class Foo: pass
# ...
# >>> foo = Foo()
# >>> class Bar(object): pass
# ...
# >>> bar = Bar()
# >>> type(Foo)
# <type 'classobj'>
# >>> type(foo)
# <type 'instance'>
# >>> type(Bar)
# <type 'type'>
# >>> type(bar)
# <class '__main__.Bar'>

