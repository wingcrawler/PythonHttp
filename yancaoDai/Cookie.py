import urllib2
import cookielib

url = 'http://220.189.236.198/cunet/indexaction.do?method=init'
#定义cookie

filename = 'cookie.txt'
cookies = cookielib.MozillaCookieJar(filename)
#定义保存了cookie的opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
#定义请求
request = urllib2.request_host()
response = None
try:
    response = urllib2.urlopen(url,timeout=3)
except urllib2.URLError as e:
  if hasattr(e, 'code'):
    print 'Error:',e.code
  elif hasattr(e, 'reason'):
    print 'Reason:',e.reason
finally:
  if response:
    image_data = response.read()
    image_stream = open('../file/code.png','wb')
    image_stream.write(image_data)
    image_stream.close()





#定义响应
response = opener.open(request)
#保存cookie到文件
cookies.save(ignore_discard=True, ignore_expires=True)
#得到已经保存的cookie
