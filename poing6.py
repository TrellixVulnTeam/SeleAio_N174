from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.set_page_load_timeout(50)
driver.get("http://asia.com")
# driver.find_element_by_name("q").send_keys("IT Company in Bankok")
# driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").send_keys(Keys.ENTER)
ids = driver.find_element_by_xpath('//*[@href]')
for i in ids:
    print(i.get_attribute("href"))



time.sleep(10)
driver.quit()
        
    

