# -*- coding:UTF-8 -*-
from sqlalchemy import ForeignKey, Column, Integer, String, func, select
from sqlalchemy.orm import relationship

from third_module.sqlalchemy_test import Base
# from sqlalchemy_test.model.user import User


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50),nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
    
    def __repr__(self):
        print("<Address(email_address = '%s')>" % self.email_address


    @classmethod
    def new_address(cls,session,email_address,user_id):
        ins = Address.__table__.insert().values(email_address=email_address,user_id=user_id)
        result = session.execute(ins)
        return result.inserted_primary_key

    @classmethod
    def find_all(cls, session):
        # sel = select([Address]).where(and_(Address.user_id == 1, Address.email_address == 'jack@google.com'))
        sel = select([Address]).where((Address.user_id == 1) & (Address.email_address == 'jack@google.com'))
        c = select([func.count('1')]).select_from(sel.as_scalar().alias())

        record = session.execute(sel).fetchall()
        count = session.execute(c).fetchone()[0]

        return record, count