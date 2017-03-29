import urllib2
import TimeUnil
import time


def DownLoad(
        url='https://omeo.alipay.com/service/checkcode?sessionID=fe66e06042064e11ce07250a20406af8&r=0.002703446697811973'):
    response = None
    try:
        response = urllib2.urlopen(url, timeout=1)
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'Error:', e.code
        elif hasattr(e, 'reason'):
            print 'Reason:', e.reason
    finally:
        if response:
            FileName = TimeUnil.timeFileFormat() + "vaildCode.jpg";
            image_data = response.read()
            # print image_data
            image_stream = open('../file/zhifubao/' + FileName, 'wb')
            image_stream.write(image_data)
            image_stream.close()


def Beach(i):
    j = 0
    while j < i:
        j = j + 1
        print j
        DownLoad()


Beach(20)
