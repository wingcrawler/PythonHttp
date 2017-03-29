# coding=utf-8
__author__ = 'Xuexianwu'

import urllib2, re, os, datetime
from selenium import webdriver

# 这是一些配置 关闭loadimages可以加快速度 但是第二页的图片就不能获取了打开(默认)
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = False
cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
driver = webdriver.PhantomJS(desired_capabilities=cap)

# driver.add_cookie({'name': 'JSESSIONID', 'value': 'DFA09A33B8D4FE696F9FEA81A2C027B6'})

driver.get("http://operate.lemonjinfu.com/")


response = driver.page_source

print(response)
