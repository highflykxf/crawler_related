# -*- coding:utf-8 -*-
import sys,string,types
import mechanize
import cookielib
from bs4 import BeautifulSoup
from random import randint
from time import sleep

file= open('movie_list',"rb");
for name in file:
    br = mechanize.Browser()        #br是模拟的浏览器
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # setting
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # br.set_debug_http(True)
    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')]
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    # Open the login page

    br.open('http://movie.douban.com/') #打开豆瓣电影页面
    br.select_form(nr=0)        #选一个表
    br.form['search_text']=name.decode('utf-8') #输入要查询的电影的名字
    br.submit()                #提交
    result = br.response()        #返回结果
    linkss = [l for l in  br.links()] #把浏览器链接加入linkss列表中
    rr = br.follow_link(linkss[36])   #点击搜索结果的第一条  这个21是尝试出来的，因为上面还有注册等等链接
    #print rr.read()
    type_of_movie='<span class="pl">类型:</span> '  #手动找标签，也可以返回的源文件，用beautifulsoup解析
    zhipiandi_of_movie ='<span class="pl">制片国家/地区:</span>'
    #print br.title()
    ss=rr.read().split('\n')
    for line in ss:
        if line.find(type_of_movie)>0 or line.find(zhipiandi_of_movie)>0:
            print line
    br.close()