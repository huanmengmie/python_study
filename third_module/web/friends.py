# -*- coding:UTF-8 -*-
import cgi

reshtml = '''
Content-Type:text/html\r\n
<html>
    <head>
        <title>脚本返回的页面</title>
    </head>
    <body>
        <h3>姓名：<i>%s</i></h3><br>
        好友个数：<b>%d</b>
    </body>
</html>
'''

form = cgi.FieldStorage()
who = form['name'].value
number = form['number'].value
print(reshtml % (who, number))