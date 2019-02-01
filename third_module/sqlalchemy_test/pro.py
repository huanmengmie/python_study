# -*- coding:UTF-8 -*-

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

reload(sys)
sys.setdefaultencoding('utf-8') 
engine = create_engine('mysql+mysqldb://root:admin@localhost:3306/python_study?charset=utf8',echo = True)
DbSession = sessionmaker(bind = engine)
session = DbSession()

