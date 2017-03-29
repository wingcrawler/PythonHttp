import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "D:\Crawler\WebDriver\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://www.wdzj.com/dangan/htyd/dianping/")

print(driver.page_source)

element=driver.find_element_by_link_text("")

driver.close()
driver.quit()
