# -*- coding: utf-8 -*-

"""

네이버 API를 이용한 '8퍼센트' 블로그 검색 결과
포스팅 작성 날짜 기준 : 이틀 전까지 

"""

import os
import sys
import urllib.request
import datetime
from datetime import date, timedelta
import time
import json
from config import * # 개발자 등록 후 - API 키, 시크릿 키 입력 
from blog_cralwer import * 

# app_id = ""
# secret_id = ""

# [CODE 1]

def get_request_url(url):
    print(">get_request_url()")
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", secret_id)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]

def getNaverSearchResult(sNode, search_text, page_start, display):
    print(">getNaverSearchResult()")
    base = "https://openapi.naver.com/v1/search" # get results in blog
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)
    url = base + node + parameters

    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)


# [CODE 3]

def getPostData(post, jsonResult):
    print(">getPostData()")

    title = post['title']
    description = post['description']
    # org_link = post['postdate']
    link = post['bloggerlink']

    # Tue, 14 Feb 2017 18:46:00 +0900

    # pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    # pDate = pDate.strftime('%m/%d')

    pDate = post['postdate']

    jsonResult.append({'title': title, 
                        'description': description,
                    #    'org_link': org_link, 
                       'link': link,
                       'pDate': pDate,
                       })
    return


def main():

    print(">main()")
    jsonResult = []

    # choose search category : 'news', 'blog', 'cafearticle'

    sNode = 'blog'

    # search_text = input("검색할 키워드 입력 (ex.8퍼센트, 에잇퍼센트) => ")
    search_text = ui.keyword # blog_crawler.py에서 keyword값을 받는다. 
    display_count = 100 # maximum, the number of results

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    while ((jsonSearch != None) and (jsonSearch['display'] != 0)):
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open('%s_%s.json' % (search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('%s_%s.json이 저장되었습니다.' % (search_text, sNode))

    jsonData = open('%s_%s.json' % (search_text, sNode), "r", encoding="utf-8").read()

    data = json.loads(jsonData) 

    for idx in range(len(data)) :

        if data[idx]["pDate"] >= (date.today() - timedelta(2)).strftime('%Y%m%d') : # 이틀 전까지 작성된 포스팅만 보기

            return (
                "\n\n",
                "날짜 :" + data[idx]["pDate"] + "\n", 
                "\n타이틀 :" + data[idx]["title"].replace("<b>","").replace("</b>","") + "\n",
                "\n요약 :" + data[idx]["description"].replace("<b>","").replace("</b>","") + "\n",
                "\n링크 :" + data[idx]["link"].replace("?Redirect=Log&amp;logNo=","/") + "\n\n",
                )   


# if __name__ == '__main__':
    # main()

