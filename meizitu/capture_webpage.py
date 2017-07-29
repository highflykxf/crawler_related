#-*- coding:utf-8 -*-
##导入requests
import requests
##导入bs4中的BeautifulSoup
from bs4 import BeautifulSoup
import os
##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"}
##开始的URL地址
all_url = 'http://www.mzitu.com/all'
##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
start_html = requests.get(all_url,  headers=headers)
##打印出start_html (请注意，concent是二进制的数据，一般用于下载图片、视频、音频、等多媒体内容是才使用concent, 对于打印网页内容请使用text)
print(start_html.text)
