# -*- coding:UTF-8 -*-

from sqlalchemy import Column, Integer, String, select, exists, and_
from sqlalchemy.orm import relationship

from third_module.sqlalchemy_test import Base
from third_module.sqlalchemy_test import Address


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(20))
    addresses = relationship(
        "Address", order_by=Address.id, back_populates="user")

    def __repr__(self):
        return "<User(id = '%d',name = '%s', fullname = '%s', password = '%s'" % (
        self.id, self.name, self.fullname, self.password)


    @classmethod
    def find_user_with_email(cls,session,id):
        # ins = session.query(User).filter(exists().where(User.id == Address.user_id))
        # for item in ins:
        #     print(item
        ins = select([User]).where(and_(User.id == id,exists().where(User.id == Address.user_id)))
        return session.execute(ins)