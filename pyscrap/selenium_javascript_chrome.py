from selenium import webdriver

driver = webdriver.Chrome('C:/Users/roseline/chromedriver/chromedriver')
driver.implicitly_wait(3)

driver.get("http://en.wikipedia.org")

driver.execute_script("window.alert('Hello World')")

# print(Res)
