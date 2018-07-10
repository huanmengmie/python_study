# -*- coding:UTF-8 -*-
""" 数字相关知识 """

# 五种基本数字类型：
# 1、有符号整型 （int）    0101   84 -234  0x80 017 -439  -0X92
# 2、长整型     （float）  24320L   -43543     0xABCDDABDCFAL
# 3、布尔型     （bool）   True    False
# 4、浮点值     （float）  3.2343   4.2E-10 -1.34E-19
# 5、复数       （complex）6.23+1.4j   -1.34-875j  -0.22+0j

# Python支持的数字类型
# 整型、长整型、布尔型、双精度浮点型、十进制浮点数、复数

# 混合模式操作符
#  1 + 1 = 2
#  '1' + '1' = '11'
#  1 + '1'    # 报错
#  1.0 + 1 = 2.0

#  数据转换
#  复数 》 浮点数  》 长整型  》  普通整型

# 算术操作符
#   单目运算符：正号（+）和负号（-）
#   双目运算符：+、-、*、/、%、**（幂运算）、//（整除）

#  / 和 //
#  /   对整型进行除操作时，返回整型（地板除）；对浮点型除操作时，会进行真正的除法
#  //  不管操作何种数据，都是执行地板除

# 使用 from __future__ import division 引入真正的除法
# from __future__ import division
# 1 / 2     #0.5

# 奇葩的幂运算符，优先级高于左侧操作数一元操作符，低于右侧操作数一元操作符
#  3 ** 2       》  9
#  -3 ** 2      》  -9
#  (-3) ** 2    》  9
#  4 ** -1      》  0.25


# 位操作符
#  取反（~ ）、按位与（&）、或（|) 、异或（^ )、左移（<< )、右移（ >> )
#  优先级      取反（~ ） 》 左移（<< )、右移（ >> )  》  加减    》   按位与（&）、或（|) 、异或（^ )

# 标准类型函数
# cmp()、str()、type()在数字对象中用来比较大小、转换为字符串、返回数字对象类型等

# 数字类型函数
#   转换工厂函数：int()、long()、float（）、complex（）、bool()  用来转换数据类型
#       工厂函数：指这些内建函数都是类对象，当调用该工厂函数，实际上创建了一个类实例

#   功能函数：abs()、coerce()、divmod()、pow()、round()
#   abs()返回绝对值
#   coerce()数据类型转换函数，返回一个包含类型转换完毕的两个数值元素的元组
#           coerce( 1, 2.5)  => (1.0,2.5)    coerce( 1j ,134L)   =>  ( 1j , 134 + 0j)
#   divmod()返回商和余数的元组               divmod(10,3)   =>  (3,1)
#   pow()进行指数运算
#   round(x, y)四舍五入运算,返回浮点数。y是其小数位数

# pow() 和 **
# pow() 是函数，** 是操作符

# int()、Math.floor()和round（）
# int()截掉小数部分，整数型
# Math.floor()向下取整，浮点型
# round() 四舍五入，浮点型


#  仅用于整型的函数
#  进制转换 oct()转8进制， hex()转16进制
#  ASCII转换   chr()整型转字符，ord()字符转整型
