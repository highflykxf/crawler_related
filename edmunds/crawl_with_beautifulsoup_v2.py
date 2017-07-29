# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

url = 'https://www.edmunds.com/acura/mdx/2009/suv/consumer-reviews/pg-2/'

try:
    #设置chrome选项：不加载图片
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    #设置timeout时间
    driver.set_page_load_timeout(3000)
    driver.set_script_timeout(3000)
    driver.get(url)
    webpage_content = driver.page_source
    soup = BeautifulSoup(webpage_content, "html.parser")
    review_container = soup.find_all('div',class_="individual-review-container")
    for container in review_container:
        overall_contents = container.find_all('div',class_="individual-overal-rating")[0]
        rating_value = overall_contents.find_all('span',itemprop="ratingValue")[0].get('title')
        review_title = overall_contents.find_all('span',class_="reviewTitle")[0].string
        individual_review_stars_container = container.find_all('div',class_="individual-review-stars-container")[0]
        rating_detail_list = individual_review_stars_container.find_all('span',class_="")
        author = container.find_all('strong',class_="author-crr")[0].string
        date_time = container.find_all('time')[0].string
        review_content = container.find_all('review-text')[0].string

        print "overall_rating: "+rating_value
        print "review_title: "+review_title
        print "author: "+author
        print "date_time: "+date_time
        for item in rating_detail_list:
            rating_aspect = item.text.split()
            rating_score = item.find_all('span',class_="rating-big star-alignment")[0].get('title').split()
            print str(rating_aspect) + " : " + str(rating_score)

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason





#自定义过滤函数
#print soup.find_all(has_class_but_no_id)
