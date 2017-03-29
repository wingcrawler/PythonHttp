import urllib2
import TimeUnil
import time
import thread


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
            print image_data
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


# Beach(100)
DownLoad()
