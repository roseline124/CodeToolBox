"""
수강 신청하기 
"""

# https://portal.hanyang.ac.kr/sugang/sulg.do

from selenium import webdriver
import time
import random 

myID = 'guseod24'
myPW = 'skanf30715'

driver = webdriver.Chrome('C:/Users/roseline/chromedriver/chromedriver')

#open url
driver.get('https://portal.hanyang.ac.kr/sugang/sulg.do')
driver.implicitly_wait(random.random()*2)
time.sleep(1)

#login popup
login_button = driver.find_element_by_id('btn-user2')
login_button.click()
driver.implicitly_wait(random.random()*2)

#login ID
login_id = driver.find_element_by_xpath("//*[@id=\"pop_login\"]/form/div[1]/div/div[1]/fieldset/p[1]/input") #error
login_id.clear()
login_id.send_keys(myID)
driver.implicitly_wait(random.random()*1)

#login PW
login_pw = driver.find_element_by_xpath("//*[@id=\"pop_login\"]/form/div[1]/div/div[1]/fieldset/p[2]/input") #error
login_pw.clear()
login_pw.send_keys(myPW)
driver.implicitly_wait(random.random()*1)

#login submit 
login_submit = driver.find_element_by_css_selector("#pop_login > form > div.popup_section > div > div.login_default > fieldset > p.btn_login > a") #error
login_submit.submit()
print("로그인 버튼 클릭")


# go to hope class tab 
hope_button = driver.find_element_by_xpath('//*[@id="snb"]/ul/li[5]')
hope_button.click()
driver.implicitly_wait(random.random()*1)

#wait until the server time is on time 
