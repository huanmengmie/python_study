# -*- coding:UTF-8 -*-

import numpy as np
from numpy import newaxis

# 创建ndarry
print(np.array([1, 2, 43, 5]))
# => array([ 1,  2, 43,  5])
print(np.arange(15).reshape((3, 5)))
# => array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
print(np.zeros((3, 5), "int32"))
# => array([[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]])
print(np.ones((2, 3, 4), 'complex'))
# => array([[[1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j],
#         [1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j],
#         [1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j]],
#        [[1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j],
#         [1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j],
#         [1.+0.j, 1.+0.j, 1.+0.j, 1.+0.j]]])
print(np.arange(10, 30, 5))
# => array([10, 15, 20, 25])
print(np.linspace(0, 20, 7))
# => array([ 0.        ,  3.33333333,  6.66666667, 10.        , 13.33333333,  16.66666667, 20.        ])
print(np.empty((2, 3)))
# => array([[ 3.33333333,  6.66666667, 10.        ],
#        [13.33333333, 16.66666667, 20.        ]])

# --------------------- 基本运算 --------------------------

a = np.arange(0, 40, 10)

b = np.arange(4)

print("转数组", a.tolist())
print("a + b = ", a + b)
print("a - b = ", a - b)
print("a * b = ", a * b)
print("a / b = ", a / b)
print("np.sin(a) = ", np.sin(a))
print("b ** 2 = ", b ** 2)
print("b < 2 = ", b < 2)

c = np.arange(1, 7).reshape(2, 3)
d = np.arange(10, 16).reshape(3, 2)

print("矩阵按元素直接相乘", np.arange(1, 7).reshape(2, 3) * np.arange(11, 17).reshape(2, 3))
print("矩阵乘法：c @ d", c @ d)
print("矩阵乘法：c.dot(d)", c.dot(d))

# += , *= 更新原有的值，不会创建新的变量
d += np.arange(6).reshape(3, 2)
print(d)

# 当不同精度的数据进行运算，结果为高精度数据
a1 = np.ones(3, dtype=np.intc)
b1 = np.linspace(0, np.pi, 3)
c1 = a1 + b1
print("a1，b1, c1的数据类型分别是:", a1.dtype.name, b1.dtype.name, c1.dtype.name)

# 计算所有数据，忽略形状
a2 = np.random.random((3, 4))
print("a2.sum() = ", a2.sum())
print("a2.min() = ", a2.min())
print("a2.max() = ", a2.max())

# 计算指定行列的数据
print("按行求和", a2.sum(axis=1))
print("按列求和", a2.sum(axis=0))
print("按行累计求和", a2.consum(axis=1))
print("按列累计求和", a2.consum(axis=0))

# 形状转换，不会改变原有数据
a3 = np.array(10 * np.random.random((3, 4)))
print("原型", a3)
print("一维数组", a3.ravel())
print("二维变形", a3.reshape(2, 6))
print("行列转换", a3.T)
# 形状转换，改变原有数据
a3.resize((6, 2))
print("形状转换，改变原有数据", a3.resize())

# 不同数组，存储在一起
a4 = np.floor(10 * np.random.random((2, 3)))
b4 = np.floor(5 * np.random.random((2, 3)))

print("按行存储", np.hstack((a4, b4)))
print("按列存储", np.vstack((a4, b4)))

# column_stack 和 row_stack 有不同的玩法
a = np.array([4., 2.])
b = np.array([3., 8.])
print("返回二维数组", np.column_stack((a, b)))  # returns a 2D array
# =》 array([[ 4., 3.],
#       [ 2., 8.]])
print(np.hstack((a, b)))  # the result is different
# =》 array([ 4., 2., 3., 8.])
print(a[:, newaxis])  # this allows to have a 2D columns vector
# =》 array([[ 4.],
#       [ 2.]])
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
# =》 array([[ 4.,  3.],
#       [ 2.,  8.]])
print(np.hstack((a[:, newaxis], b[:, newaxis])))  # the result is the same
# =》 array([[ 4.,  3.],
#       [ 2.,  8.]])

# 将一个大数组分割成多个小数组
a = np.floor(10*np.random.random((2,12)))
print("切割为3个数组", np.hsplit(a, 3))
print("切割3份 前3个，第4个，其余", np.hsplit(a, (3, 4)))
print("切割4份 前3个，第4个，第5、6, 其余", np.hsplit(a, (3, 4, 6)))


# ------------------ 复制和视图 ----------------------

a = np.arange(12)
print("a原来的样子", a)
# 木有copy
b = a
print("a 和 b 的内存地址相等？", id(a) == id(b))  # True
b.shape = (3, 4)
print("a的shape也改变了", a)

# 浅copy
c = a.view()
print("a 和 c 的内存地址相等？", id(a) == id(c))  # False
print("c.base is a", c.base is a)  # True

c.shape = (2, 6)
c[0, 4] = 1234
print("a的数据", a)

# 深copy
d = a.copy()
print("d.base is a", b.base is a)  # False
d[0, 0] = 94
print(a)
