# -*- coding: utf-8 -*-
"""
- xx：公有变量
- _xx：单前置下划线，私有化属性或方法，无法通过from some_module import *导入，
类对象和子类可以访问
- __xx：双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问(名字重整)
- __xx__：双前后下划线，用户名字空间的魔法对象或属性(少用)
- xx_：单后置下划线，用于避免与Python关键词冲突(最好不用)

名字重整(name mangling)：防止子类意外重写基类方法或者属性，可以通过_Class__object
机制访问private属性

"""
name_outer = "李四"
__nation_outer__ = "China"
__sex_outer = "woman"
address_outer__ = "浦东新区"

_mobile_outer_ = "17612844"
_age_outer = 1823
mail_outer_ = "234@163.com"


class MethodModifier(object):

    __nation__ = "China"
    __sex = "man"
    address__ = "浦东"

    _mobile_ = "17612123844"
    _age = 18
    mail_ = "234234@163.com"

    name = "张三"

    def __init__(self, name):
        self.name = name

    def show_sex(self):
        print(self.__sex)


if __name__ == '__main__':
    m = MethodModifier("张三")
    print(m.name)
    print(m.address__)
    print(m.mail_)
    print(m._age)
    print(m.__nation__)
    print(m._MethodModifier__sex)


