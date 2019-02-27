from bs4 import BeautifulSoup # 클래스

html = """

<html>

<body>

<h1> 스크래핑 연습 </h1>

</body>

</html>

"""

#html 분석하기
soup = BeautifulSoup(html, 'html.parser') # 클래스로부터 만들어진 객체 # 분석기

# h1태그 내용에 접근
h1 = soup.html.body.h1

# h1 요소의 내용 추출
print("h1=", h1.string)
