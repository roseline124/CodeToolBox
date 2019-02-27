from bs4 import BeautifulSoup
import requests
#세션을 사용하는 경우

session = requests.session() # 세션 시작

#로그인 하기

login_info = {
    "id":'uesrID',
    "pw":'uesrPW'
}

url = "http://www.test.com/login.php"
#id와 pw를 확인하는 페이지
#id와 pw를 확인하는 로직 : 서버단 스크립트

result = session.post(url, data = login_info)

#오류 체크 : 예외 처리
result.raise_for_status()

#로그인 후, get 방식으로 서비스 요청
myUrl ="http://www.test.com/mypage.html"
res = session.get()
res.raise_for_status()

soup = BeautifulSoup(res.text,"html.parser")
#res의 데이터를 text 형식으로 받겠다.
