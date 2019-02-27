import requests
import json #보통 웹 API 결과는 json, XML 형식으로 리턴

#API 키 지정
apikey = "24d129cfecb6c544fdb22ac0bd3be928"

#어떤 도시의 정보?
city_list = ["Seoul,KR", "Tokyo,JP", "New York,US"]

#API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APIID={key}"
#매개변수 q는 도시 이름 저장, apiid는 api키 저장

#켈빈 온도를 섭씨 온도로 변환하는 함수
k2C = lambda k: k -273.15

for name in city_list:

    #API의 url 구성하기
    url = api.format(city=name                                     , key=apikey) #json 형태로 반환됨

    #api요청을 보내 날씨 정보를 가져오기
    res = requests.get(url)

    #JSON 형식 데이터를 파이썬 데이터로 변환
    data = json.loads(res.text)

    #결과 출력
    print("**도시 = ", data["name"])
    print("|날씨 = ", data["weather"][0]["descreption"])
    print("|최저 기온 = ", k2C(data["main"]["temp_min"]))
    print("|최고 기온 = ", k2C(data["main"]["temp_max"]))
    print("|습도 = ", data["main"]["humidity"])
