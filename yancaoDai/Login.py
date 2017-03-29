import urllib
import urllib2
import cookielib
import re
import base64

# from bs4 import BeautifulSoup

# 此处代码假定已经获得验证码解析为7788

# 登录地址
loginurl = 'http://www.zjhzyc.com/indexaction.do?method=init'
# 定义cookie
filename = 'cookie.txt'
cookies = cookielib.MozillaCookieJar(filename)
# 登录发送参数

a = '33010120141112142A'
b = '123456'

postdataa = base64.b64encode(a)
postdatab = base64.b64encode(b)

postdata1 = urllib.urlencode({
    'formusercode': postdataa,
    'formuserpassword': postdatab,
    'formusertype': '1',
    'formconfirmpassword': '7788'})

# 登录头部信息
loginHeaders = {
    'Host': 'www.zjhzyc.com',
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Connection': 'Keep-Alive'
}

# 定义保存了cookie的opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
# 定义请求
request = urllib2.Request(loginurl, postdata1, loginHeaders)
# 定义响应
response = opener.open(request)
# 保存cookie到文件
cookies.save(ignore_discard=True, ignore_expires=True)
# 得到已经保存的cookie
cookies.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 跳转订单页面
urlorder = 'http://www.zjhzyc.com/elonlineindentaction.do?method=order&index=33'
# 定义查询参数
orderdata = {
    'formbegindate': 20150101,
    'formenddate': 20150131,
    'formpagerecord': 100,
    'formpageno': 1
}
# 订单查询
requestodo = urllib2.Request(urlorder)
requestod = urllib2.Request(urlorder, orderdata)
respodo = opener.open(requestodo)
respod = opener.open(requestod)
odo = respodo.read()
odlist
page = respod.read()

# 假定此处已经获得全年订单号，存放在列表odlist中
f = open(r'detail.txt', 'w')
f
for i in range(len(odlist)):
    f.write(opener.open(urllib2.Request(
        'http://www.zjhzyc.com/elonlineindentaction.do?method=orderdetail&ordersid=' + str(odlist[i])).read(), "\r\n")
    f.close()

    # 最后用正则表达式或者beautifulsoup剔除记录文本中的多余代码
