# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content">(.*?)</div>.*?<div class="stats.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print "author: "+item[0]
        print "content: "+item[1].strip()
        print "like num: "+item[2]
        print "comment num: "+item[3]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
