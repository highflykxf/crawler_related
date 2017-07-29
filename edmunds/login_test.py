# -*- coding:utf-8 -*-
import urllib2
import re
page = 1
url = 'https://www.edmunds.com/acura/mdx/2009/suv/consumer-reviews/pg-1/#991536896400785408-anchor'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/53.0.2785.116 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="(.*?)">.*?', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
