# -*- coding:UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

from sqlalchemy_use.model.address import Address
from sqlalchemy_use.model.user import User


reload(sys)
sys.setdefaultencoding('utf-8')     # 将ascii编码改为utf-8编码


engine = create_engine('mysql+mysqldb://root:admin@localhost:3306/python_study?charset=utf8',echo = True)
# engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)


# session = sessionmaker(bind = engine)()
DbSession = sessionmaker(bind = engine)
session = DbSession()

# 添加方法
# user = User(name='test', fullname='EdJones', password='edspassword')
# user.addresses = [Address(email_address='jack@google.com'),
#                 Address(email_address='j25@yahoo.com')]
# session.add(user)
#
# session.add_all([User(name='三少', fullname='唐家三少', password='123456'),
#                  User(name='东哥',fullname='辰东',password='123456'),
#                  User(name='土豆',fullname='天蚕土豆',password='123456')])
#
# user.name = 'test'
#
# print 'dirty',session.dirty
# print 'new',session.new
# specialUsers = session.query(User).filter(User.name.in_(['ed',"三少"])).all()       # in
# print 'specialUsers',specialUsers
#

# add = Address()
# id = add.new_address(session,'skdfjl@163.com',3)
# print id
# lists = add.find_all(session)
# print lists
u = User()
res = u.find_user_with_email(session,1)
for item in res:
    print item
session.commit()

# 查询方法
# specialUsers = session.query(User).filter(~User.name.in_(['ed',"三少"])).all()       # not in
# print 'not specialUsers',specialUsers
#
# for item in session.query(User).order_by(User.id)[3:5]:
#     print item
