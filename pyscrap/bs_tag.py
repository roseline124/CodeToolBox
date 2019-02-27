from bs4 import BeautifulSoup as bsoup
import urllib.request as req

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

#urlopen()으로 url 가져오기
res = req.urlopen(url)

#웹 데이터 분석하기
soup = bsoup(res, "html.parser")

#데이터 찾기 #find
wf = soup.find("wf").string

print(wf)
