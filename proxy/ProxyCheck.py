# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


# check proxy eg: {"http": 'http://some-proxy.com:8080'}
def check(proxy):
    # print proxy
    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    response = None
    url = 'http://1212.ip138.com/ic.asp'
    try:
        a = datetime.now()
        response = urllib2.urlopen(url, timeout=2)
        b = datetime.now()
        print (b - a).microseconds
        if response.getcode() == 200:
            soup = BeautifulSoup(response.read().decode('GBK'), "xml")
            trs = soup.select('body')[0].get_text().strip()
            print trs
            return True
        else:
            return False
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print 'Error:', e.code
        elif hasattr(e, 'reason'):
            print 'Reason:', e.reason
        return False
    except Exception as ec:
        if hasattr(ec, 'code'):
            print 'Error:', ec.code
        elif hasattr(ec, 'reason'):
            print 'Reason:', ec.reason
        return False
