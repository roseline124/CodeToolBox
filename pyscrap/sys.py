import sys
import urllib.request as req # 매번 모듈명을 쓰기 귀찮으니 별명을 req로 정해 사용하겠다. #as = alias
import urllib.parse as parse

#명령줄 인수가 제대로 입력되었는지 확인

if len(sys.argv) <= 1: # 명령줄 인수가 1 이하이면, 오류 메시지 출력
    print("python 인수1 인수2")
    sys.exit()

regionCode = sys.argv[1] #2번째 변수

rssUrl = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnid' : '133'
}

params = parse.urlencode(values)

url = rssUrl + "?" + params

print("url=", url)

# rss 데이터 다운

data = req.urlopen(url).read()
text = data.decode("utf-8")

print(text)
