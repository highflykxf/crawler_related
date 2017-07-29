import urllib2
import urllib

values = {"username":"18201023809","password":"18201023809kxf"}
data = urllib.urlencode(values)
url = "https://login.sina.com.cn/"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
headers = {'User-Agent':user_agent}
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()