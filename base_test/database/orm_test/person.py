# -*- coding: utf-8 -*-
from base_test.database.orm_test.base import Base


class Person(object, metaclass=Base):

    table_name = "person"

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
