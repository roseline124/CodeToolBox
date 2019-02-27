import random
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('auto-open-devtools-for-tabs')
driver = webdriver.Chrome('C:/Users/roseline/chromedriver/chromedriver', options=options)
driver.implicitly_wait(2)



driver.get('https://www.together.co.kr/menu/index.php?menu=main')

button = driver.find_element_by_id('p_banner_section_close')
button.click()
driver.implicitly_wait(random.random() * 2)
time.sleep(5)

scroll_button = driver.find_element_by_xpath('//*[@id="fp-nav"]/ul/li[3]/a')
scroll_button.click()
driver.implicitly_wait(2)
time.sleep(5)

target = driver.find_element_by_id('total_loan_amount')
print(target.text)