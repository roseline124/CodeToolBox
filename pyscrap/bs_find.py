from bs4 import BeautifulSoup # 클래스

html = """

<html>

<body>

<h1 id="title"> 스크래핑 연습 </h1>

</body>

</html>

"""

#html 분석하기
soup = BeautifulSoup(html, 'html.parser') # 클래스로부터 만들어진 객체 # 분석기

#find() 메서드 사용

title = soup.find(id="title")
print("title=", title.string)
