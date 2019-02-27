# execute_script() 메서드를 이용한 자바스크립트 활용

from selenium import webdriver

driver = webdriver.PhantomJS('C:/Users/roseline/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)

driver.get("https://google.com")
res = driver.execute_script("return 10+10")
print(res)
