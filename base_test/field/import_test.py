# -*- coding: utf-8 -*-
from python_study.base_test.field.declare import MethodModifier


m = MethodModifier("张三")
print(m.name)
print(m.address__)
print(m.mail_)
print(m._age)
print(m.__nation__)
print(m._MethodModifier__sex)

from python_study.base_test.field.declare import _age_outer, _mobile_outer_,\
    __sex_outer, name_outer, __nation_outer__, mail_outer_, address_outer__

# print(_age_outer)
# print(_mobile_outer_)
# print(__sex_outer)
# print(__nation_outer__)
# print(name_outer)
# print(mail_outer_)
# print(address_outer__)


# 通过 from .. import * 无法导入_object形式的变量，第一个字符为_都无法导入
from python_study.base_test.field.declare import *
print(_age_outer)   # unresolved
print(_mobile_outer_)  # unresolved
print(__sex_outer)  # unresolved
print(__nation_outer__)  # unresolved
print(name_outer)
print(mail_outer_)
print(address_outer__)

