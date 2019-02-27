from selenium import webdriver
import urllib.request
import urllib.parse 
import random
import time

#open webdriver
# t_driver = webdriver.Chrome('C:/Users/roseline/chromedriver/chromedriver')
# t_driver.implicitly_wait(random.random()*3)

na_driver = webdriver.Chrome('C:/Users/roseline/chromedriver/chromedriver')
na_driver.implicitly_wait(random.random()*3)

"""
Tistory Login
"""
def T_login(_url, my_id, my_pw) :

    #접속
    t_driver.get(_url)
    t_driver.implicitly_wait(random.random()*2)


    #ID / PW
    inputID = t_driver.find_element_by_xpath('//*[@id="loginId"]')
    inputID.clear()
    inputID.send_keys(my_id)
    time.sleep(random.random()*0.5)

    inputID = t_driver.find_element_by_xpath('//*[@id="loginPw"]')
    inputID.clear()
    inputID.send_keys(my_pw)
    time.sleep(random.random()*0.5)

    #로그인 
    submitLogin = t_driver.find_element_by_xpath('//*[@id="authForm"]/fieldset/button')
    submitLogin.submit()
    t_driver.implicitly_wait(random.random()*2)


"""
네이버 블로그 게시물 복사 
: 블로그 내의 요소에 접근할 수 없다는 에러 : unable to search element ...
다른 프레임 내에 있기 때문 : driver.switch_to.frame("frameID")  # 프레임 바꿔주기 


"""
def get_feed(_url) :

    na_driver.get(_url)
    na_driver.implicitly_wait(random.random()*2)

    #Category
    cat_button = na_driver.find_element_by_class_name('_folderToggle _returnFalse _param(parentcategoryno_21) f_icoopen')
    cat_button.click()

    cat_list2 = na_driver.find_element_by_xpath('//*[@id="category40"]').text

    cat_list3 = na_driver.find_element_by_xpath('//*[@id="category39"]').text
    
    print("Category List :", cat_list2)
    print("Category List :", cat_list3)

    # for i in range() :
    #     print("Page ",i, ": ")
    #     for j in range(5) : 
    #         _list = na_driver.find_element_by_xpath('//*[@id="listTopForm"]/table/tbody/tr[',j,']/td[1]/div/span/a')
    #         print("No.", j, ".", _list) 

    # post_url = input("which contents do you want to copy?")

    # na_driver.find_element_by_xpath('//*[@id="listTopForm"]/table/tbody/tr[5]/td[1]/div/span/a')

login_url = 'https://www.tistory.com/auth/login'
na_blog_url = 'https://blog.naver.com/guseod24'

my_id = 'guseod24@gmail.com'
my_pw = 'roseline124!'


# T_login(login_url, my_id, my_pw)
get_feed(na_blog_url)






# na_url = 'https://blog.naver.com/guseod24' 
# t_url = 'https://roseline124.tistory.com/'

"""
#ID / PW
inputID = na_driver.find_element_by_xpath('//*[@id="id"]')
inputID.clear()
#한 글자씩 입력하도록 하는 법
for i in range(len(my_id)) : 

    inputID.send_keys(my_id[i])
    time.sleep(random.random()*0.5)
"""

#selenium binding 참고 
# https://selenium-python.readthedocs.io/locating-elements.html



