# -*- coding:utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = "http://search.jd.com/Search?keyword=%E7%99%BD%E9%85%92&enc=utf-8&wq=%E7%99%BD%E9%85%92&pvid=dabb02927c1e4ef3a26a04d0a1d0df9a"
html = urllib.urlopen(url).read()
price_table = pd.DataFrame(np.array(['名称','价格']).reshape(1,2),columns=['name','price'])
soup = BeautifulSoup(html, "html.parser")
for each_div in soup.find_all('div', {"class":"gl-i-wrap"}):
    commodity_attrs = each_div.text
    price =  each_div.find_all("div",{"class":"p-price"})[0].text.strip()\
        # , each_div.find_all('strong',{"class"})
    name = each_div.find_all("div",{"class":"p-name p-name-type-2"})[0].text.strip()
    data = pd.DataFrame([(price,name)], columns=['price','name'])
file_name = 'commodity&price.csv'
price_table.to_csv(file_name,header=False,index=False)