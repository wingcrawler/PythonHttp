import urllib2
import TimeUnil
import time


def DownLoad(url='http://www.bjgjj.gov.cn/wsyw/servlet/PicCheckCode1'):
    response = None
    try:
        response = urllib2.urlopen(url)

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
            image_stream = open('../file/bjgjj/_' + FileName, 'wb')
            image_stream.write(image_data)
            image_stream.close()


def Beach(i):
    j = 0
    while j < i:
        j = j + 1
        time.sleep(0.9)
        DownLoad()
        print j



Beach(210)
