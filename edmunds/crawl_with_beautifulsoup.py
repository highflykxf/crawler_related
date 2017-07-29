# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

url = 'https://www.edmunds.com/acura/mdx/2009/suv/consumer-reviews/pg-2/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
             '(KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, "html.parser")
    review_container = soup.find_all('div',class_="individual-review-container")
    for container in review_container:
        overall_contents = container.contents[1]
        rating_big = overall_contents.contents[1].contents[1].get('title')
        review_title = overall_contents.contents[3].string
        individual_review_stars_container = container.find_all('div',class_="individual-review-stars-container")[0]
        rating_detail_list = individual_review_stars_container.find_all('span',class_="")
        author = container.find_all('strong',class_="author-crr")[0].string
        date_time = container.find_all('time')[0].string

        print "overall_rating: "+rating_big
        print "review_title: "+review_title
        print "author: "+author
        print "date_time: "+date_time
        for item in rating_detail_list:
            rating_aspect = item.nextSibling
            rating_score = item.get('title')
            print rating_aspect + " : " + rating_score

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason





#自定义过滤函数
#print soup.find_all(has_class_but_no_id)
