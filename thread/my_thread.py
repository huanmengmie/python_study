# -*- coding:UTF-8 -*-
""" threading.Thread类的派生子类 """
import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        
    
    def getResult(self):
        return self.res
    
    
    def hello(self):
        print 'hehe'
    
    def run(self):
        print 'starting',self.name,'at:',ctime()
        self.res = apply(self.func,self.args)
        print self.name,'finished at ',ctime()