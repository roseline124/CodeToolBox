import json

#json 데이터

price = {
    "time" : "17-01-02",
    "price" : {
        "apple": 1000,
        "banana": 3000,
        "orange": 2000
    } #객체 안에 객체를 더 넣을 수 있다.
}

#json.dumps메서드는 json 형식으로 출력하는 메서드
jsonData = json.dumps(price)#위의 딕셔너리 구조를 파이썬으로 출력하겠다.

print(jsonData)
