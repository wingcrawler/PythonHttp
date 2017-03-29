# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import base64
from OCR import image_linux
from bs4 import BeautifulSoup
from httpclient import MybeautifulSoup
from urlparse import *
import time
from httpclient import MysqlDB
from dateUtil import date_List

# 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.zjhzyc.com/baloginaction.do?method=check')


# for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value

# 跳转订单页面
def oreder_request(begin_date, end_date):
    urlorder = 'http://www.zjhzyc.com/elonlineindentaction.do?method=orderquery&index=32'
    # 定义查询参数
    orderdata = {
        'formbegindate': begin_date,
        'formenddate': end_date,
        'formpagerecord': '100',
        'formpageno': 1
    }

    data = urllib.urlencode(orderdata)
    # 订单查询
    # requestodo = urllib2.Request(urlorder)
    requestding = urllib2.Request(url=urlorder, data=data)
    # respodo = opener.open(requestodo)
    respod = opener.open(requestding)
    # odo = respodo.read()
    page = respod.read().decode('GBK')
    # print page
    resultList = MybeautifulSoup.parse_table(page)

    print resultList
    # MysqlDB.insert(resultList)

    # soup = BeautifulSoup(page, "xml")
    # print soup.select("table#table1 > tr")
    # print page.decode('GBK')


url = 'http://www.zjhzyc.com/public/public/validimg.jsp'
req = urllib2.Request(url)
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
if response:
    image_data = response.read()
    image_stream = open('D:\\Crawler\\OCR\\court_temp\\hz.png', 'wb')
    image_stream.write(image_data)
    image_stream.close()
    imagecode = image_linux.image_ocr('D:\\Crawler\\OCR\\court_temp\\hz.png')

    print imagecode
    imagecode = filter(str.isalnum, imagecode)
    print imagecode
    if len(imagecode) > 4:
        print  'imagecode error'
        imagecode = filter(str.isalnum, imagecode)
        print 'fliter after\t' + imagecode
    if len(imagecode) < 4:
        print 'fliter after  error !!!\t' + imagecode
        # for item in cookie:
        #     print 'Name = ' + item.name
        #     print 'Value = ' + item.value
    print 'imagecode processor end'
    if len(imagecode) == 4:
        # 登录地址
        loginurl = 'http://www.zjhzyc.com/baloginaction.do?method=check'
        # 定义cookie
        filename = 'cookie.txt'
        cookies = cookielib.MozillaCookieJar(filename)
        # 登录发送参数

        a = '33010120131230076A'
        b = '123456'
        postdataa = base64.b64encode(a)
        postdatab = base64.b64encode(b)
        postdata1 = urllib.urlencode({
            'formusercode': postdataa,
            'formuserpassword': postdatab,
            'formusertype': '1',
            'formconfirmpassword': imagecode})

        # 登录头部信息
        loginHeaders = {
            'Host': 'www.zjhzyc.com',
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Connection': 'Keep-Alive'
        }

        # 定义保存了cookie的opener
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # 定义请求
        request = urllib2.Request(loginurl, postdata1, loginHeaders)
        # 定义响应
        response = opener.open(request)
        time.sleep(1)
        # print response.read().decode('GBK')

        for item in cookie:
            print item.name
            print item.value
            if (item.name == 'usercode'):
                print 'login in sucess'
                dateList = date_List()
                for m in dateList:
                    print m[0]
                    print m[1]
                    oreder_request(m[1], m[0])
