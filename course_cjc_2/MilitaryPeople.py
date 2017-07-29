import urllib2
f=urllib2.urlopen('http://military.people.com.cn/n/2013/0705/c1011-22087628.html')
print f.read().lower()