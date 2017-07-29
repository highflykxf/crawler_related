# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


soup = BeautifulSoup(html,"lxml")

print soup.find_all('b')

for tag in soup.find_all(True):
    print tag.name,": ",tag.string

#自定义过滤函数
print soup.find_all(has_class_but_no_id)

print soup.find_all(id='link2')
#传入href参数，beautifulsoup会搜索每个tag的“href”属性
print soup.find_all(href=re.compile("elsie"))
#使用多个指定名字的参数可以同时过滤tag的多个属性
print soup.find_all(href=re.compile("elsie"),id='link1')
#使用class过滤（class为python关键词）
print soup.find_all("a",class_="sister")
#有些tag属性在搜索不能使用，比如HTML5中的data-*属性
#可以通过find_all()方法的attrs参数定义一个字典参数来搜索包含特殊属性的tag

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
#print data_soup.find_all(data-foo="value")
print data_soup.find_all(attrs={"data-foo":"value"})

#通过 text 参数可以搜搜文档中的字符串内容.
# 与 name 参数的可选值一样, text 参数接受
# 字符串 , 正则表达式 , 列表, True
print soup.find_all(text="Elsie")
# [u'Elsie']

print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# [u'Elsie', u'Lacie', u'Tillie']

print soup.find_all(text=re.compile("Dormouse"))
[u"The Dormouse's story", u"The Dormouse's story"]