import urllib.request
import urllib.parse #url을 인코딩하기 위해 불러오는 모듈

rssUrl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp" #모든 지역의 기상정보 불러온다.

#매개변수 : 지역별 코드를 지정하는 변수
#파이썬 자료 구조 중 Dictionary 이용
#stnid 코드 : 108 전국, 109 수도권, 133 충청도, 105 강원도

values = {
    'stnid':'108'
}

#parsing 작업

params = urllib.parse.urlencode(values)

url = rssUrl + "?" + params

print("url=", url)

# 데이터 가져오기

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8") #utf-8형식으로 보여달라

print(text)
