from bs4 import BeautifulSoup as bsoup

html = """

<html>

<body>

<h1> 스크래핑 연습 </h1>
<h1> 스크래핑 연습2 </h1>

</body>

</html>

"""

#html 분석하기
soup = bsoup(html, 'html.parser') # 클래스로부터 만들어진 객체 # 분석기

#모든 h1 태그 데이터를 갖고 오고 싶다.

# h1 = soup.html.body.h1 #기존 방식
# print("h1=", h1.string) # 첫번째 요소 하나만 갖고 온다.

h1 = soup.find_all("h1")

for a in h1: #a라는 변수에 h1 값을 하나하나 넣겠다.
    text = a.string
    #href = a.attrs # 변수 뒤에 데이터 타입까지 같이 써준다. 
    print(text)
