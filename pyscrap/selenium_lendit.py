from selenium import webdriver

#드라이버 가져오기
driver = webdriver.PhantomJS('C:/Users/roseline/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)

#렌딧 페이지 on
driver.get("https://invest.lendit.co.kr/invest")

loan = driver.find_element_by_xpath('//*[@id="pageContent"]/div/section[2]/h3/em')
#총 대출액 찾기
loan_data = loan.text

print(loan_data)
