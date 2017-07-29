import sys
import urllib
import urllib2
import cookielib

reload(sys)
sys.setdefaultencoding("utf8")

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
    'userName':'kongxiangfei2015@ia.ac.cn',
    'pwd':'xiangfei'
})
login_url = 'http://jwxk.ucas.ac.cn/dlogin'
#user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
#headers = {'User-Agent':user_agent}
result = opener.open(login_url,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
grade_url = 'http://jwxk.ucas.ac.cn/score/yjs/all'
result = opener.open(grade_url)
print result.read()