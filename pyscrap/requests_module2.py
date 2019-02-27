#이미지 데이터 가져오기

import requests

res = requests.get("https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png")

#바이너리 형식으로 이미지 저장

with open("logo.png","wb") as f:
    f.write(res.content)

print("이미지 저장")
