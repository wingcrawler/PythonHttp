#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import TimeUnil
import time
import thread
from bs4 import BeautifulSoup

def DownLoad():
    url = 'http://www.smgjj.com/CheckCode.aspx?i=0'
    response = None
    try:
        response = urllib2.urlopen(url, timeout=5)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'Error:', e.code
        elif hasattr(e, 'reason'):
            print 'Reason:', e.reason
    finally:
        if response:
            FileName = TimeUnil.timeFileFormat() + "vaild.jpg";
            image_data = response.read()
            soup = BeautifulSoup(image_data, "lxml")  # 指定文档解析器
            info = soup.img['src']
            print info
            DownLoad2('http://www.smgjj.com/'+info)
            # image_stream = open('../file/smgjj/' + FileName, 'wb')
            # image_stream.write(image_data)
            # image_stream.close()


def DownLoad2(url):
    # url = 'http://www.smgjj.com/CheckCode.aspx?i=0'
    response = None
    try:
        response = urllib2.urlopen(url, timeout=5)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'Error:', e.code
        elif hasattr(e, 'reason'):
            print 'Reason:', e.reason
    finally:
        if response:
            FileName = TimeUnil.timeFileFormat() + "vaild.jpg";
            image_data = response.read()
            # soup = BeautifulSoup(image_data, "lxml")  # 指定文档解析器
            # info = soup.select('img')
            # print info
            image_stream = open('../file/smgjj/' + FileName, 'wb')
            image_stream.write(image_data)
            image_stream.close()


def Beach(i):
    j = 0
    while j < i:
        j = j + 1
        print j
        time.sleep(0.9)
        thread.start_new_thread(DownLoad,())


Beach(200)
# DownLoad()
