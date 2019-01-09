# -*- coding:UTF-8 -*-
""" 序列相关 """
from string import Template
# 标准类型操作符
#   A、对象值比较
#      <  >   <=  >=  ==  !=  <>
#   B、对象身份比较，是否为同一对象
#      is    is not
#   C、布尔类型
#      not  》  and  》  or

# 序列类型操作符
#   A、成员关系操作符（in ,not in)       '123' in 'sldkfj123kljfds'      => True
#   B、连接操作符（+）                   'hello' + ' world'              => 'hello world'
#   C、重复操作符（*）                   'abc' * 2                       => 'abcabc'
#   D、切片操作符（[],[:],[x:y:z])         y的值要比x大，z为步长

print('asdfsbcd'.find('m'))
print('asdfsbcd'.rindex('bc'))

# 成员关系操作符in 、not in 和 rfind()、rindex()、find()、index（）
# in 、not in是操作符，判断一个字符（串）是否出现在另一个字符串中
# rfind()、rindex()、find()、index（）是函数用来判断一个字符串是否包含另一个字符串，包含则返回其下标，否则返回-1

str = 'abcdefg'
i = -1
for i in range(-1, -len(str), -1):
    print(i, str[:i])

for i in [None] + range(-1, -len(str), -1):
    print(i, str[:i])

# 内建函数（BIF）
# list（iter）        将可迭代对象转换为列表
# str(obj)            将对象转换为str
# unicode(obj)        将对象转换为unicode字符串
# basestring()        抽象工厂函数，是str和unicode的基类，不能被实例化和调用
# tuple(iter)         将可迭代对象转换为元组

# 序列类型可用的内建函数
# enumerate（iter)
# len(seq)
# max(iter,key=None)            max('ldkzjfls')  =>  z
# min(iter,key=None)
# reversed(seq)
# sorted(iter,func=None,key=None,reverse=False)
# sum(seq,init=0)
print(zip('abc', '123', 'xyz'))  # =>  [('a', '1', 'x'), ('b', '2', 'y'), ('c', '3', 'z')]

aList = [1, 2, 3, '4', 2]
print(aList.__sizeof__())

# 字符串拼接的方法
# A、使用连接符 +
print('hello' + ' world')
# B、使用字符串格式化操作符 %
str = '%s %s' % ('hello', 'world')
print(str)
# C、使用join（）方法，将列表拼接为字符串，分隔符为调用方法的内容
s = '_'.join(('hello', 'world', '!'))  # =>  hello_world_!
# D、使用字符串模板   from string import Template


str = Template('${name}今年${age}岁了')
print(str.substitute(name='张三', age='19'))
print(str.safe_substitute(name='李四', age='29'))

# substitute()和safe_substitute()方法
try:
    print(str.substitute(age='20'))  # 安全性高，缺少参数时会报KeyError的错
except KeyError as e:
    print(e)
print(str.safe_substitute(age='23'))  # 安全性低，原样输出   =》 ${name}今年23岁了

# 一些只适用于字符串的操作符
# A、格式化字符串 %
# B、原始字符串操作符 r/R     >> print(r'\n\tsklfjdsf')       =>    \n\tsklfjdsf

import re

m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print(m.group())
m = re.search(r'\\[rtfvn]', r'Hello World!\n')
if m is not None:
    print(m.group())

str2 = 'hello world'
print(str2.endswith('d'))
print(str2.find('or', 3))

a = [2, 34, 4, ]
b = (12, 34, 5, 2)
print(a, b)

# 列表

# 列表比较
#   先比较列表中的第一个值，如果值相等就继续向下比较，直到不相等的情况出现，或者到达较短序列的末尾。
#       1、对两个列表的元素进行比较
#       2、同类型，比较其值
#       3、不同类型，检查是否为数字
#           a、如果是数字，执行必要的数字强制类型转换看，然后比较
#           b、如果一方为数字，则另一方大（数字是最小的）
#           c、否则，通过类型名字的字母顺序进行比较
#       4、如果一个列表首先达到末尾，则另一个长一点的列表大
#       5、如果列表中所有元素相等，则两个列表相等，返回0
