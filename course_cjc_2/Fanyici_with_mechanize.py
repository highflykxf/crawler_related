#! coding:utf-8
import re
import sys
import mechanize
import cookielib
from  bs4 import BeautifulSoup


def parseHtml(html):
    '''
    @summary: 抓取结构化数据
    '''
    content = ""
    wordpattern = '<h1>(.+?)的反义词</h1>'
    pattern = '<span class="medium b">(.+?)</span>'
    temp = re.findall(pattern, html)
    wordtemp = re.search(wordpattern, html)
    if temp:
        word = wordtemp.group(1)
        content = word + '\t'
        for key in temp:
            content += key + '\t'

    content = content.strip('\t')
    return content


def saveData(data):
    '''
    @summary: 数据存储
    '''
    f = open('test', 'w')
    f.write(data)
    f.close()


br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)  ##关联cookies

###设置一些参数，因为是模拟客户端请求，所以要支持客户端的一些常用功能，比如gzip,referer等
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

###这个是degbug##你可以看到他中间的执行过程，对你调试代码有帮助
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

br.addheaders = [('User-agent',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')]

r = br.open(sys.argv[1])
query = sys.argv[2]

br.select_form(nr=0)
br.form['q'] = query
br.submit()
html = br.response().read()
data = parseHtml(html)
print data
if data != "":
    saveData(data)