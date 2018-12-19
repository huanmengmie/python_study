# -*- coding:UTF-8 -*-
""" 使用unicode 字符串"""

hello = u'''
hello!
\u00A1Hola!
\u4F60\u597D!    
'''

print 'Content-Type: text/html; charset=utf-8\r'
print
print '<html><head><title>你好</title></head>'
print '<body>'
print hello.encode('utf-8')
print '</body></html>'

import random
random.choice()
