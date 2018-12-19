# -*- coding:UTF-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy_use.model.address import Address
from sqlalchemy_use.model.user import User

reload(sys)
sys.setdefaultencoding('utf-8') 
engine = create_engine('mysql+mysqldb://root:admin@localhost:3306/python_study?charset=utf8',echo = True)
DbSession = sessionmaker(bind = engine)
session = DbSession()

