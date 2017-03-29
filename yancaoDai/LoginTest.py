# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import cookielib
import re

import base64

# 声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
# 此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://220.189.236.198/cunet/indexaction.do?method=init')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

url = 'http://220.189.236.198/cunet/public/public/validimg.jsp'
req = urllib2.Request(url)
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open(req)
if response:
    image_data = response.read()
    image_stream = open('../file/loginTest.png', 'wb')
    image_stream.write(image_data)
    image_stream.close()

    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value

# 登录地址
loginurl = 'http://220.189.236.198/cunet/baloginaction.in?method=check'
# 定义cookie
filename = 'cookie.txt'
cookies = cookielib.MozillaCookieJar(filename)
# 登录发送参数

a = '36202379'
b = '168'
postdataa = base64.b64encode(a)
postdatab = base64.b64encode(b)
code = input("x: ")
postdata1 = urllib.urlencode({
    'formusercode': postdataa,
    'formuserpassword': postdatab,
    'formusertype': '1',
    'formconfirmpassword': code})

# 登录头部信息
loginHeaders = {
    'Host': 'www.zjhzyc.com',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Connection': 'Keep-Alive'
}

# 定义保存了cookie的opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 定义请求
request = urllib2.Request(loginurl, postdata1)
# 定义响应
response = opener.open(request)

print response.read()

for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value
