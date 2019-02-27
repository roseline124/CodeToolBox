"""

네이버 API 블로그 검색 결과 확인 

"""

import os.path #파일 지정
import json
from datetime import date, timedelta
from naverAPI_search import *

# search 
# if __name__ == '__main__':
#     main()

jsonData = open('%s_naver_%s.json' % ('8퍼센트', 'blog'), "r", encoding="utf-8").read()

data = json.loads(jsonData) 

for idx in range(len(data)) :

    if data[idx]["pDate"] >= (date.today() - timedelta(2)).strftime('%Y%m%d') : # 이틀 전까지 작성된 포스팅만 보기
        
        print(
            "\n\n",
            "날짜 :" + data[idx]["pDate"] + "\n", 
            "\n타이틀 :" + data[idx]["title"].replace("<b>","").replace("</b>","") + "\n",
            "\n요약 :" + data[idx]["description"].replace("<b>","").replace("</b>","") + "\n",
            "\n링크 :" + data[idx]["link"].replace("?Redirect=Log&amp;logNo=","/") + "\n\n",
            )   


