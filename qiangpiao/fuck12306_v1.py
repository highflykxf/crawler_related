# -*- coding:utf-8 -*-
from splinter.browser import Browser
from time import sleep
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#Global variable
#set the username and password
username = u"kxf13408580324"
passwd = u"kxf18201023809lx"
#set the cookies of initial address
starts_station = u"%u5317%u4EAC%2CBJP"
ends_station = u"%65B0%u4E61%2CXXF"
#set the time format
dtime = u"2017-01-20"
# the train number
order = 0
#set passenger name
passenger_name = u"孔祥飞"
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"


# login the website
def login():
    browser.find_by_text(u"登录").click()
    sleep(3)
    browser.fill("loginUserDTO.user_name",username)
    sleep(1)
    browser.fill("userDTO.password", passwd)
    sleep(8)


#购票
def huoche():
    global browser
    browser = Browser(driver_name="chrome")
    browser.visit(ticket_url)
    while browser.is_text_present(u"登录"):
        sleep(1)
        login()
        if browser.url == initmy_url:
            break

    try:
        print u"购票页面。。。"
        # 跳回购票页面
        browser.visit(ticket_url)
        browser.cookies.add({"_jc_save_fromDate": dtime})  # 此处添加出发日期
        browser.cookies.add({"_jc_save_fromStation": starts_station})  # 此处添加出发地
        browser.cookies.add({u'_jc_save_toStation': ends_station})  # 此处添加目的地
        browser.reload()
        sleep(2)
        count = 0
        if order != 0:
            while browser.url == ticket_url:
                browser.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询。。。 第%s次"%count
                sleep(1)
                try:
                    browser.find_by_text(u"预定")[order-1].click()
                except:
                    print u"还没开始预订"
                    continue
        else:
            while browser.url == ticket_url:
                browser.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in browser.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)
        browser.find_by_text(passenger_name)[1].click()
        print  u"能做的都做了.....不再对浏览器进行任何操作"
    except Exception as e:
        print traceback.print_exc()

if __name__ == "__main__":
    huoche()
    # browser = Browser(driver_name="chrome")
    # # ##注意不要去掉http://
    # # browser.visit("https://www.google.com.hk/webhp?hl=zh-CN")
    # # browser.fill("wd","splinter")
    # browser.visit(login_url)
    # # browser.find_by_text(u"登录").click()
    # print u"等待验证码，自行输入。。。"
    # while True:
    #     if browser.url != initmy_url:
    #         sleep(1)
    #     else:
    #         break
    #
    # browser.visit(ticket_url)
