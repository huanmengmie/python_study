# -*- coding:UTF-8 -*-

# 动态类型
# 对象的类型和内存占用都是在运行时确定

# 内存分配

# 引用计数
# 1、计数增加
#     对象被创建   x = 3.12
#     别名被创建     y = x
#     作为参数传递给函数（新的本地引用）   foobar(x)
#     成为容器对象中的元素       myList = [123, x, 'ads']

# 2、计数减少
#     本地引用离开了其作用范围，如foobar(x)方法执行完毕
#     对象别名被显示销毁       del x
#     对象被从一个窗口对象中移除   myList.remove(x)
#     窗口对象本身被销毁      del myList