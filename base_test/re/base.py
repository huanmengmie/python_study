# -*- coding:UTF-8 -*-
import re


def re_test():
    a = re.findall("测试", "这是一个测试啊")
    m = "一个测试"
    pattern = "".join(["(<em>)?({})(<\/em>)?".format(item) for item in m])
    checked_content = re.sub(pattern, double, "这是一个<em>测试</em>这是<em>一个测试</em>")
    print(checked_content)


# 将匹配的数字乘以 2
def double(matched):
    print(matched)
    return "<em>{}</em>".format(matched.group(0))


def complex_re():
    """
    参考：https://www.runoob.com/regexp/regexp-tutorial.html
    非贪婪匹配：当?紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的
    (?:pattern) 非捕获匹配 (?:<pp>)
    (?!pattern) 正向否定匹配  ((?!<A)
    (?<!pattern) 逆向否定匹配  ((?<!aa)
    :return:
    """
    content_re = re.compile(r"<DD>(?:<pp>)?((?!<A).*?)(?:</pp>)?</DD>", re.S)
    a = "<DD><pp>自行车的人正在得意洋洋地脱把前行。<br /></pp></DD>"
    b = "<DD>自行车的人正在得意洋洋地脱把前行。<br /></DD>"
    print(content_re.findall(a))
    print(content_re.findall(b))


if __name__ == '__main__':
    re_test()