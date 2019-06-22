#-*-coding:utf-8

from selenium import webdriver
from time import sleep
import bs4

def control_button(YEAR):
    # 주간 선택 버튼 
    week_button = driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/table/tbody/tr[1]/td/a[2]/img')
    week_button.click()
    sleep(0.5)

    year = driver.find_element_by_xpath(f'//*[@id="s_year"]/option[{YEAR}]') 
    year.click()
    sleep(0.5)    

def search_news(WEEK):
    week = driver.find_element_by_xpath(f'//*[@id="s_week"]/option[{WEEK}]')  
    week.click()
    sleep(0.5)

    search_button = driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/table/tbody/tr[4]/td[2]/a/img')
    search_button.click()
    sleep(0.5) 

def parse_page():
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, 'html.parser')
    
    tags = soup.find_all("a")
    txt = [t.getText().strip() for t in tags]
    
    return txt

def collect_news(txt):
    week_headlines = []
    
    # empty인 경우 
    if txt[140] == '':
        return week_headlines.append([]*7)

    for n in range(1,8):
        if n == 7 : 
            curr_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n}]/h4/a').text
            curr_idx = txt.index(curr_week)
            check = txt[curr_idx+1]

            if check != '':
                headlines = txt[curr_idx+1:curr_idx+20]
                week_headlines.append(headlines)
            else :     
                week_headlines.append([])

        else :
            curr_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n}]/h4/a').text # div2 / 1~7 주까지 있다
            next_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n+1}]/h4/a').text 
            curr_idx = txt.index(curr_week)
            next_idx = txt.index(next_week)

            headlines = txt[curr_idx+1:next_idx]

            week_headlines.append(headlines)

    return week_headlines

def collect_res_news(txt, check):
    week_headlines = []

    # empty인 경우 
    if txt[140] == '':
        return week_headlines.append([]*7)
    
    for n in range(1,check+1):
        if n == check : 
            curr_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n}]/h4/a').text
            curr_idx = txt.index(curr_week)
            check = txt[curr_idx+1]

            if check != '':
                headlines = txt[curr_idx+1:curr_idx+20]
                week_headlines.append(headlines)
            else :     
                week_headlines.append([])

        else :
            curr_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n}]/h4/a').text # div2 / 1~7 주까지 있다
            next_week = driver.find_element_by_xpath(f'//*[@id="news-rank"]/div[{n+1}]/h4/a').text 
            curr_idx = txt.index(curr_week)
            next_idx = txt.index(next_week)

            headlines = txt[curr_idx+1:next_idx]

            week_headlines.append(headlines)

    return week_headlines

def get_all_headlines(YEAR, WEEK):
    """
    년단위 주별 HOT 뉴스 크롤링
    """
    control_button(YEAR)
    
    WEEK += 6
    TIME = (52-WEEK)//7
    check = 52 - (WEEK + 7*TIME)

    # 검색
    all_headlines = []
    
    for n in range(TIME+1):
        search_news(WEEK + 7*n)

        txt = parse_page()
        week_headlines = collect_news(txt)
        all_headlines.append(week_headlines)

    # 나머지 뉴스
    search_news(52)
    txt = parse_page()
    week_headlines = collect_res_news(txt, check)
    all_headlines.append(week_headlines)

    return all_headlines

# =================================================
# MAIN 로직
# warning! 133번 라인의 크롬드라이버 주소 변경할 것
# =================================================

URL = "http://newsrank.hani.co.kr/"

driver = webdriver.Chrome("C:\chrome\chromedriver.exe") # 크롬드라이버 주소 바꾸기 

driver.get(URL)
sleep(1)

# 상수
YEAR = 14 # 13 : 2016년, 14 : 2017년, 15 : 2018년, 16 : 2019년 
WEEK = 1 # 1 : 첫주부터, 23 : 6월부터 

all_heads = get_all_headlines(YEAR, WEEK)

with open("han_heads.data", "w", encoding = "utf-8") as f :
    f.write(str(all_heads))

print("끝!")