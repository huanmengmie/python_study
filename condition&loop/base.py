# -*- coding:UTF-8 -*-
""" Python 中的控制和循环 """

# a = raw_input("a =>: ")
# b = raw_input("b =>: ")
a = 3
b = 6
if a > b:
    print a, '>', b
elif a < b:
    print b, '>', a
else:
    print "="


# 三元操作符
m = 5
n = 4
x = m if m > n else n
print x

# while 循环
count = 0
while count < 5:
    count += 1
    print 'the index is ', count

# for in 循环
for i in 'abcdde':
    print i,
print

# 在while循环和for循环中使用else语句
#   else语句只在循环完成后执行，break语句也会跳过else语句块
def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest factor of %d is %d' % (num , count)
            break
        count -= 1
    else:
        print num, 'is prime'

for eachNum in range(10,21):
    showMaxFactor(eachNum)

# 列表解析   [expr for iter_var in iterable if cond_expr]
a = [(x, y, z) for x in range(2, 6) for y in range(x, 7) for z in range(y, 9)]
print 'a',a

b = [x for x in range(12) if x % 2]
print 'b',b

# 生成器表达式    (expr for iter_var in iterable if cond_expr)
# 生成器表达式是列表解析的扩展，是一个特定的函数，允许你返回一个值，然后“暂停”代码的执行，稍后恢复
rows = [1,2,3,17]


def cols():
    yield 56
    yield 12
    yield 3

x_product_pairs = ((i,j) for i in rows for j in cols())
print '生成器表达式x_product_pairs：',x_product_pairs
for pair in x_product_pairs:
    print pair

# 生成器表达式与列表解析非常相似，语法基本相同；
# 但是它并不真正的创建数字列表，而是返回一个生成器，这个生成器每次计算出一个条目后，将这个条目“产生”（yield）出来。
# 生成器表达式使用“延迟计算”（lazy evaluation），所以它在使用内存上更有效
