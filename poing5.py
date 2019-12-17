from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.get('https://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys('تکواندو ')
search.submit()

while True:
    next_page_btn =driver.find_elements_by_xpath("//a[@id='pnnext']")
    if len(next_page_btn) <1:
        print("no more pages left")
        break
    else:
        urls = driver.find_elements_by_xpath("//*[@class='iUh30']")
        mail =driver.find_elements_by_name('Email')
        urls = [url.text for url in mail]
        print(urls)

    element =WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable((By.ID,'pnnext')))
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    element.click()