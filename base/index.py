# -*- coding: utf-8 -*-

""" 操作符、数据类型、字符串、元组、执行流程"""

# print 'hello,hq'
# a = raw_input('a: ')
# b = raw_input('b: ')
# int(a)/int(b)

# 算术操作符   + - * ** / // %

# * 普通的乘法
# ** 表示阶乘


# print 'hello,hq'
# a = raw_input('a: ')
# b = raw_input('b: ')
# int(a)/int(b)

# raw_input() 输入的参数为字符串类型， == 进行值判断
# a = raw_input('input a: ')
# b = 1
# c = '1'
# print 0 == .0
# print a == b
# print b == c
# print a == c

# 五种基本数字类型：
# 1、有符号整型 （int）    0101   84 -234  0x80 017 -439  -0X92
# 2、长整型     （float）  24320L   -43543     0xABCDDABDCFAL
# 3、布尔型     （bool）   True    False
# 4、浮点值     （float）  3.2343   4.2E-10 -1.34E-19
# 5、复数       （complex）6.23+1.4j   -1.34-875j  -0.22+0j

# 简单整型和字符串对象是不可变对象会被Python缓存，即常量

# 字符串
# lan = 'python'
# print 'first letter is ;'+lan[0]
# print lan[2:]
# print lan[2:5]                  # 两个索引之间的字符
# print lan[:3] + lan[-1]  # 字符串截取
# print lan[0] * 3 + lan[-2]
# lanb = "python"
# print lan == lanb

# 单引号，双引号，三引号的使用
# print ''a''  #语法错误
# print '单引号换行时' \
#       '需要加斜杠'
# print '"a"'
# print '''slkdfjdk
#     dflskjfk
#     sdfsl;kfsf'''
# 语句跨行方式
# 1、使用 \
# 2、闭合操作符()，[],{}等
# 3、三引号包括下的字符串

# 列表和元组
# 列表用[],元素个数及元素值可以改变
# 元组用（），看做只读列表

# aList = [1,3,5,'5',1.0]
# aList.remove(5)
# print aList
# print aList[2] == aList[3]  # false
# print aList[0] == aList[4]  # true
# print aList[:3]
# print aList[2:]

# aTuple = ('robots', 22, 54, 'try')
# print aTuple
# print aTuple[:2]
# print aTuple[3:]
# aTuple[0] = 1

# 字符串之间，数字之间可以正常比较，两者混合以后字符串比较大
# x = 5
# y = '3'
# z = '5'
# print x > y      #false
# print y < z      #true

# 字典 （key-value)
# aDict = {'name': 'Tom', 'age': 18}
# aDict['sex'] = 'male'
# print aDict
# print aDict.keys()
# print aDict['name']
# for key in aDict.keys():
#     print key,aDict[key]


# if语句
# if 3 > 4:
#     print 1
# else:
#     print 0

# if-elif-else 语句
# x = raw_input("input x:")
# y = raw_input("input y:")
# if x > y:
#     print "x is bigger than y"
# elif x < y:
#     print "y is bigger than x"
# else:
#     print "they are equals"

# while循环
# count = 0
# while count < 5:
#     print 'loop #%d' % count
#     count += 1

# for 循环
# aList = [2, 3, '5', 1.0]
# for a in aList:
#     print a,      # 使用print输出，默认自动换行。在元素后边加“，”以后就不会自动换行
# print 10
#
# print 'I like to use internet for:'
# for item in ['e-mail','video','game']:
#     print (item + ' ') * 3

# range(x) 内建函数,小于X
# for item in range(4):
#     print item * 2
#
# for word in 'abcdefg':
#     print word,
# print len('abcdefg')  # len()字符串长度

# range() 和 len()联用
# str = 'myName'
# for item in range(len(str)):
#     print str[item], '(%d)' % item
# print

# enumerate()函数
# str = 'myName'
# for item, content in enumerate(str):
#     print item, content

# 列表解析
# aList = [ x ** 3 for x in range(10) if x % 2 == 0]
# print aList

# 赋值
# 普通赋值： =
# 增量赋值： +=    -=   *=     /=      %=      **=
#           <<=     >>=       &=  ^=      |=
# 多重赋值：
# x = y = z = 1
# print x,y,z,x==y==z
# 多元赋值：   变量交换
# x,y,z = 1, 3, 'ab'
# print x, y, z
# x,y = y,x
# print x,y,z
