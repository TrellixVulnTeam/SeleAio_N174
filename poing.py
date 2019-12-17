from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.set_page_load_timeout(50)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("IT Company in Bankok")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").send_keys(Keys.ENTER)
# driver.maximize_window()
# driver.refresh()
time.sleep(5)
driver.find_elements_by_tag_name('a')
mail =driver.find_elements_by_name('Email')
print(mail)
# first_link=driver.find_element_by_xpath("/html/body/div[8]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/a[1]/h3/span").click()
# email = first_link.find_element_by_xpath("//div[@id='Content']/div/div/div/div[2]/div/div/div[13]/div/div/div/div[4]/div/div/div/p/span/u/a").get_attribute('hr‌​ef')
# print(email)
# driver.send_keys(Keys.ARROW_DOWN)
# que.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
# que.send_keys(Keys.RETURN)



time.sleep(10)
driver.quit()
        
    

