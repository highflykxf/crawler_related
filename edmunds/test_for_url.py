# -*-coding:utf-8 -*-
import urllib2
import time
import os


if __name__ == "__main__":
    # static
    startTime = int(time.time())
    print ("-" * 6 + ' start ' + '-' * 6)

    model_file_path = '../../paperfuxian/oper/cars/data/2007/'
    output_path = './year_2009/'

    listing = os.listdir(model_file_path)
    for infile in listing:
        model_year = infile.split('_')[0]
        brand = infile.split('_')[1]
        sub_str = infile[5:]
        model_name = sub_str[len(brand)+1:].replace('_','-')
        print brand+'/'+model_name+'/'+model_year
        # output_filename = infile
        url_base = 'https://www.edmunds.com/'+brand+'/'+model_name+'/'+model_year+'/'+'consumer-reviews/pg-1'
        req = urllib2.Request(url_base)
        try:
            urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
        else:
            print "OK"
