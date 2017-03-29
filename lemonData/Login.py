# coding=utf-8
__author__ = 'Xuexianwu'
import time
import urllib2, re, os, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# 这是一些配置 关闭loadimages可以加快速度 但是第二页的图片就不能获取了打开(默认)
cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = False
cap["phantomjs.page.settings.localToRemoteUrlAccessEnabled"] = True
chromedriver = "D:\Crawler\WebDriver\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver = webdriver.PhantomJS(desired_capabilities=cap)
# driver = webdriver.Firefox()
# driver.add_cookie({'name': 'JSESSIONID', 'value': 'DFA09A33B8D4FE696F9FEA81A2C027B6'})

driver.get("http://cas.lemonjinfu.com/login")
Element1 = driver.find_element_by_tag_name("body")
print(Element1.get_attribute("outerHTML"))
response = driver.page_source

Element = driver.find_element_by_name("verificationcode")
print(Element.size)
print(Element.id)
print(Element.get_attribute("tabindex"))

print(Element.is_enabled())
print(Element.get_attribute("outerHTML"))
time.sleep(1)
Element.send_keys("")
Element.clear()

# print(response)
