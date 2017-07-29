# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import os
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
if __name__ == "__main__":
    # static
    startTime = int(time.time())
    print ("-" * 6 + ' start ' + '-' * 6)

    model_file_path = '../../paperfuxian/oper/cars/data/2007/'
    output_path = './year_2007/Reviews/'

    listing = os.listdir(model_file_path)
    for infile in listing:
        model_year = infile.split('_')[0]
        brand = infile.split('_')[1]
        sub_str = infile[5:]
        model_name = sub_str[len(brand)+1:].replace('_', '-')
        output_filename = infile
        url_base = 'https://www.edmunds.com/'+brand+'/'+model_name+'/'+model_year+'/'+'consumer-reviews/pg-'
        page = 19
        flag_first = True
        max_page_num = 10000
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' \
                     ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        headers = {'User-Agent': user_agent}

        while page <= max_page_num:
            url = url_base + str(page) + '/'
            try:
                request = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(request)
                content = response.read().decode('utf-8')

                # soup = BeautifulSoup(content, "html.parser")
                # if flag_first == True:
                #     flag_first = False
                #     last_page_str = soup.find_all('div', id="pagination-footer-listUpperFooter")[0].find_all('a')[-1].string
                #     if len(last_page_str) >= 5:
                #         num_page = int(str(last_page_str[5:]))
                #     else:
                #         num_page = int(str(last_page_str))
                #     max_page_num = num_page

                pattern = re.compile(
                    '<strong.*?class="author-crr">(.*?)</strong>.*?'
                    '<p.*?class="review-text">(.*?)</p>.*?'
                    '<p.*?class="review-text">(.*?)</p>.*?'
                    '<p.*?class="review-text">(.*?)</p>.*?',
                    re.S)
                items = re.findall(pattern, content)

                with open(output_path + output_filename + '.csv', 'a') as csvfile:
                    myfile = csv.writer(csvfile, dialect='excel')
                    for item in items:
                        author_crr = item[0]
                        review_content = item[1]
                        pros = item[2]
                        cons = item[3]
                        row_of_data = []
                        row_of_data.append(author_crr)
                        row_of_data.append(review_content)
                        row_of_data.append(pros)
                        row_of_data.append(cons)
                        myfile.writerow(row_of_data)
            except urllib2.URLError, e:
                if hasattr(e, "code"):
                    print (e.code)
                if hasattr(e, "reason"):
                    print (e.reason)
            page += 1
