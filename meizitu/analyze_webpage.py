#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os



headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
##开始的URL地址
all_url = 'http://www.mzitu.com/all'
##使用requests中的get方法来获取all_url(就是：http://www.mzitu.com/all这个地址)的内容 headers为上面设置的请求头、请务必参考requests官方文档解释
start_html = requests.get(all_url,  headers=headers)
##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
Soup = BeautifulSoup(start_html.text, 'lxml')
##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）


# li_list = Soup.find_all('li')
# ##这个不解释了。看不懂的小哥儿回去瞅瞅基础教程
# for li in li_list:
#     print(li)

##意思是先查找 class为 all 的div标签，然后查找所有的<a>标签。
all_a = Soup.find('div', class_='all').find_all('a')
# for a in all_a:
#     print(a)


# for a in all_a:
#     title = a.get_text() #取出a标签的文本
#     href = a['href'] #取出a标签的href 属性
#     print(title, href)

# for a in all_a:
#     title = a.get_text() #取出a标签的文本
#     href = a['href'] #取出a标签的href 属性
#     html = requests.get(href, headers=headers) ##上面说过了
#     html_Soup = BeautifulSoup(html.text, 'lxml') ##上面说过了
#     max_span = html_Soup.find_all('span')[10].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
#     for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
#         page_url = href + '/' + str(page) ##同上
#         print(page_url) ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！


for a in all_a:
    title = a.get_text() #取出a标签的文本
    href = a['href'] #取出a标签的href 属性
    html = requests.get(href, headers=headers) ##上面说过了
    html_Soup = BeautifulSoup(html.text, 'lxml') ##上面说过了
    max_span = html_Soup.find_all('span')[10].get_text() ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了。
    for page in range(1, int(max_span)+1): ##不知道为什么这么用的小哥儿去看看基础教程吧
        page_url = href + '/' + str(page) ##同上
        img_html = requests.get(page_url, headers=headers)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_='main-image').find('img')['src'] ##这三行上面都说过啦不解释了哦
        print(img_url)