from selenium import webdriver

user = "guseod24"
mypw = "skanf960124"

driver = webdriver.PhantomJS('C:/Users/roseline/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)

url_login="https://nid.naver.com/nidlogin.login"

driver.get(url_login) #url로 들어간다.
print("로그인 페이지 접속 완료")

#아이디, 비밀번호 입력하는 input 요소 찾고 value값 입력
inputID = driver.find_element_by_id("id") # selenium은 id에 #을 안붙여도 된다.
inputID.clear() #입력박스에 있는 텍스트 모두 지우기
inputID.send_keys(user)

inputPW = driver.find_element_by_id("pw") # selenium은 id에 #을 안붙여도 된다.
inputPW.clear() #입력박스에 있는 텍스트 모두 지우기
inputPW.send_keys(mypw)

# 로그인 버튼을 찾고 전송하기
submitLogin = driver.find_element_by_css_selector("input.btn_global[type=submit]")

submitLogin.submit()
print("로그인 버튼 클릭")

#확인하기
driver.implicitly_wait(3)
driver.save_screenshot("login_완료.png")
