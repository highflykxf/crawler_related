# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib2
import time
import os
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    # static
    startTime = int(time.time())
    print ("-" * 6 + ' start ' + '-' * 6)

    model_file_path = '../../paperfuxian/oper/cars/data/2009/'
    output_path = './year_2009/'

    listing = os.listdir(model_file_path)
    for infile in listing:
        model_year = infile.split('_')[0]
        brand = infile.split('_')[1]
        sub_str = infile[5:]
        model_name = sub_str[len(brand)+1:].replace('_', '-')
        output_filename = infile
        url_base = 'https://www.edmunds.com/'+brand+'/'+model_name+'/'+model_year+'/'+'consumer-reviews/pg-'
        # url_base = 'https://www.edmunds.com/nissan/murano/2009/consumer-reviews/pg-'
        page = 20
        flag_first = True
        max_page_num = 10000

        while page <= max_page_num:
            url = url_base + str(page) + '/'
            try:

                # cap = webdriver.DesiredCapabilities.PHANTOMJS
                # cap["phantomjs.page.settings.resourceTimeout"] = 100000
                # cap["phantomjs.page.settings.loadImages"] = False
                # cap["phantomjs.page.settings.disk-cache"] = True
                # cap["phantomjs.page.customHeaders.Cookie"] = 'SINAGLOBAL=3955422793326.2764.1451802953297; '
                # driver = webdriver.PhantomJS(
                #     executable_path="E:\\program_files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe",
                #     desired_capabilities=cap)
                # driver.set_window_size(1120, 1000000)

                # 设置chrome选项：不加载图片
                chromeOptions = webdriver.ChromeOptions()
                prefs = {"profile.managed_default_content_settings.images": 2}
                chromeOptions.add_experimental_option("prefs", prefs)
                driver = webdriver.Chrome(chrome_options=chromeOptions)
                # driver = webdriver.Chrome()
                # 设置timeout时间
                driver.set_page_load_timeout(3000)
                driver.set_script_timeout(3000)
                driver.get(url)

                webpage_content = driver.page_source
                soup = BeautifulSoup(webpage_content, "html.parser")
                if flag_first == True:
                    flag_first = False
                    last_page_str = soup.find_all('div', id="pagination-footer-listUpperFooter")[0].find_all('a')[-1].string
                    if len(last_page_str) >= 5:
                        num_page = int(str(last_page_str[5:]))
                    else:
                        num_page = int(str(last_page_str))
                    max_page_num = num_page
                review_container = soup.find_all('div', class_="individual-review-container")
                for container in review_container:
                    overall_contents = container.find_all('div', class_="individual-overal-rating")[0]
                    rating_value = overall_contents.find_all('span', attrs={"title": True})[0].get('title')
                    review_title = overall_contents.find_all('span', class_="reviewTitle")[0].string
                    individual_review_stars_container = \
                        container.find_all('div', class_="individual-review-stars-container")[0]
                    rating_detail_list = individual_review_stars_container.find_all('span',
                                                                                    class_="rating-big star-alignment")
                    author = container.find_all('strong', class_="author-crr")[0].string
                    date_time = container.find_all('time')[0].string
                    review_content = container.find_all('p', class_="review-text")[1].text
                    pros_content = container.find_all('p', class_="review-text")[2].text
                    cons_content = container.find_all('p', class_="review-text")[3].text
                    # print (str(review_content.decode('utf-8')))

                    # with open(output_path+output_filename, "a") as myfile:
                    row_of_data = []
                    with open(output_path+output_filename+'.csv', 'a') as csvfile:
                        myfile = csv.writer(csvfile, dialect='excel')
                        row_of_data.append(rating_value)
                        row_of_data.append(review_title)
                        row_of_data.append(author)
                        row_of_data.append(date_time)

                        # myfile.write("overall_rating: " + rating_value + '\n')
                        # myfile.write("review_title: " + review_title + '\n')
                        # myfile.write("author: " + author + '\n')
                        # myfile.write("date_time: " + date_time + '\n')
                        for item in rating_detail_list:
                            rating_score = item.get('title').strip()
                            row_of_data.append(rating_score)
                            # myfile.writerow([rating_aspect, rating_score])
                            # myfile.write(str(rating_aspect) + " : " + str(rating_score) + '\n')
                        # myfile.write(str(review_content.decode('utf-8')))
                        # myfile.write("\n")
                        row_of_data.append(review_content)
                        row_of_data.append(pros_content)
                        row_of_data.append(cons_content)
                        myfile.writerow(row_of_data)
                        # myfile.writerow(['review_content', review_content])
                driver.close()
            except urllib2.URLError, e:
                if hasattr(e, "code"):
                    print (e.code)
                if hasattr(e, "reason"):
                    print (e.reason)
            page += 1