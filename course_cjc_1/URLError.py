import urllib2

request = urllib2.Request('http://music.163.com')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,err:
    print err.code;
except urllib2.URLError,err:
    print err.reason
else:
    print "OK"