# -*- coding:UTF-8 -*-
"""" 字典、集合相关方法 """
# 创建字典
#   普通方法
dict1 = {'name': 'jame', 'age': '18'}
#   工厂方法 dict()
fdict = dict((['x', 1], ['y',4]))
print fdict         # =>  {'y': 4, 'x': 1}
fdict2 = dict(zip(('x', 'y'), (1, 2)))  # zip()=> [('x', 1), ('y', 2)]
print fdict2        # =>  {'y': 2, 'x': 1}
a = [('xy'[i-1], i) for i in range(1,3)]  # => [('x', 1), ('y', 2)]
fdict3 = dict(a)
print fdict3        # =>  {'y': 2, 'x': 1}

#   内建方法 fromkeys()
ddict = {}.fromkeys(('x','y','z'),-1)
print ddict         # =>    {'y': -1, 'x': -1, 'z': -1}

dic = {None: 'test','test':None}
print dic

# 字典中key和value都可以为None值，但是其key不允许重复，且必须为数字和字符串等可以哈希的对象，而不能使用列表和字典
# 值相等的数字，哈希值相等表示相同的键
# 列表和元组内的对象可以重复

# 在字典中使用字符串格式符 % 的特别用法
dic2 = {'name': 'jame', 'age': 18, 'sex': '男'}
print '%(name)s是一个%(age)d岁的%(sex)s人' %dic2

# 字典的比较方法
# 先比较字典大小，然后是键，最后是值



# 集合 无序不重复
# 可变集合 set  可以添加和删除元素
# 不可变集合  fozenset

# 集合类型操作符
#   联合      |
#   交集      &
#   差补/相对补集     -
#   对称差分        ^
#   在混合集合类型操作中，操作所产生的结果类型与左边的操作数相等

# 集合类型操作符（仅适用于可变集合）
#   （Union）update  更新                                  |=
#   Retention/Intersection update   保留/交集更新          &=
#   Different update    差更新                             -=
#   Symmetric Different Update  对称差分更新               ^=

# 集合内建函数
# 工厂函数
# set() 和frozenset()，不提供参数默认生成空集合。
# 若提供参数，则该参数必须是可迭代的，即一个序列，或迭代器，或支持迭代的一个对象。例如文件或字典