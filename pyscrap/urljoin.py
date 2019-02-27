#urllib.parse.urljoin() 함수는 상대경로를 절대경로로 변환하는 함수

from urllib.parse import urljoin

baseUrl = "http//www.example.com/html/a.html"

# urljoin(baseUrl, "b.html") #a.html 대신 b.html을 넣어주겠다.

print(urljoin(baseUrl, "b.html")) # ./b.html 로 써도 된다. (./ : 현재위치)

# urljoin(baseUrl, "sub/c.html")
print(urljoin(baseUrl, "sub/c.html"))

print(urljoin(baseUrl, "../index.html")) # ../ : 이전 폴더
