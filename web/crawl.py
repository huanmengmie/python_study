# -*- coding:UTF-8 -*-
''' 网络爬虫 '''

from sys import argv
from formatter import DumbWriter, AbstractFormatter
from htmllib import HTMLParser
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from cStringIO import StringIO


class Retriever(object):
    """ 网络爬虫 """
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)


    def filename(self,url,deffile = 'index.html'):  # 存储地址
        paserdurl = urlparse(url,'http:',0)
        print 'parsedurl',paserdurl
        path = 'D:/'+ paserdurl[1] + paserdurl[2]
        ext = splitext(path)
        if ext[1] == '':
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path)    # 本地地址
        if sep != '/':
            ldir = replace(ldir,'/',sep)
        if not isdir(ldir):
            if exists(ldir):
                unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):     # 下载网页
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError, e:
            retval = '*** ERROR: invalid URL "%s"' % self.url
        return retval

    def parseAndGetLinks(self):     # 解析HTML文档，保存链接 parse html,save links    
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist

class Crawler(object):
    count = 0
    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':    # 错误情况
            print retval, '...带有*，不解析'
            return
        Crawler.count += 1
        print '\n(%d)' % Crawler.count
        print 'URL:',url
        print 'FILE:',retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks()
        for eachlink in links:
            if eachlink[:4] != 'http' and find(eachlink, '://') == -1:
                eachlink = urljoin(url, eachlink)
            print '* ',eachlink

            if find(lower(eachlink),'mailto:') != -1:
                print '...算了吧，这个是发邮件的'
                continue

            if eachlink not in self.seen:
                if find(eachlink,self.dom) == -1:
                    print '...算了吧，不是这个域名下的'
                else:
                    if eachlink not in self.q:
                        self.q.append(eachlink)
                        print '...新的链接，添加到集合中'
                    else:
                        print '...算了吧，这个链接已经保存过了'
            else:
                print '...算了吧，已经处理过了'

    def go(self):
        while self.q:
            url = self.q.pop()
            self.getPage(url)

    def main(self):
        if len(argv) > 1:
            url = argv[1]
        else:
            try:
                url = raw_input('输入链接地址：').strip()
            except(KeyboardInterrupt, EOFError):
                url = ''
            if not url:return
            robot = Crawler(url)
            robot.go()


if __name__ == '__main__':
    craw = Crawler('')
    craw.main()
    
    
# http://www.null.com/home/index.html