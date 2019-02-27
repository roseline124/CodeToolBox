#파이썬으로 json 분석하기

import urllib.request as req
import os.path #파일 지정
import json
from datetime import date, timedelta

#json데이터 다운로드

# url = "https://api.github.com/repositories"
# fileName="rep.json"

# if not os.path.exists(url): #해당 url이 존재하는 지 확인
#     req.urlretrieve(url, fileName)

# jsonData = open('8퍼센트_naver_blog.json', "r", encoding="utf-8").read()

# data = json.loads(jsonData) #읽어온 내용을 파이썬으로 저장

# print(data)
# for dat in data:
    # print(dat)
    # print(dat["name"] + "-" + dat["owner"]["login"]) #owner밑에 login 정보를 가져오겠다. 


jsonData = open('%s_naver_%s.json' % ('8퍼센트', 'blog'), "r", encoding="utf-8").read()

data = json.loads(jsonData) #읽어온 내용을 파이썬으로 저장

# for dat in data:
    
#     if str(dat["pDate"]) >= (date.today() - timedelta(2)).strftime('%Y%m%d') : # 어제까지 작성된 포스팅만 보기 

#         print(
#             "\n\n",
#             "날짜 :" + dat["pDate"] + "\n", 
#             "\n타이틀 :" + dat["title"] + "\n",
#             "\n요약 :" + dat["description"] + "\n",
#             "\n링크 :" + dat["link"] + "\n\n",
#             )  



for idx in range(len(data)) :

    if data[idx]["pDate"] >= (date.today() - timedelta(2)).strftime('%Y%m%d') : # 이틀 전까지 작성된 포스팅만 보기
        
        print(
            "\n\n",
            "날짜 :" + data[idx]["pDate"] + "\n", 
            "\n타이틀 :" + data[idx]["title"] + "\n",
            "\n요약 :" + data[idx]["description"] + "\n",
            "\n링크 :" + data[idx]["link"] + "\n\n",
            )   