# -*- coding: utf-8 -*-
from base_test.database.pymysql_test.base import get_cursor


class Base(type):

    def __init__(cls, *args, **kwargs):
        cls.__table_name__ = cls.table_name if hasattr(cls, "table_name") else cls.__name__.lower()
        cls.attrs = {}
        for k, v in cls.__dict__.items():
            if isinstance(v, tuple):
                cls.attrs[k] = v

        for k in cls.attrs.keys():
            delattr(cls, k)
        super(Base, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Model(object, metaclass=Base):

    def save(self):
        fields = []
        args = []
        for k in self.attrs.keys():
            fields.append(k)
            args.append(getattr(self, k, None))
        args_temp = []
        for v in args:
            if isinstance(v, int):
                args_temp.append(str(v))
            elif isinstance(v, str):
                args_temp.append("""'%s'""" % v)
        sql = "insert into %s(%s) values (%s)" % (self.__table_name__, ",".join(fields), ",".join(args_temp))
        print(sql)
        return self.execute_insert(sql)

    @staticmethod
    def execute_insert(sql):
        with get_cursor() as cursor:
            cursor.execute(sql)



class Person(Model):
    table_name = "person"
    name = ("name", "varchar(50)")
    age = ("age", "int unsigned")
    sex = ("sex", "int unsigned")

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


if __name__ == '__main__':
    p = Person("张三", 18, 1)
    p.save()
