#-*-coding:utf-8

from selenium import webdriver
from time import sleep
import bs4

# ==============================
# 조선일보 스크랩 함수 
# ==============================
def scrap_chosun(SECTION, START_WEEK) :
    """
    START_WEEK : 시작 주의 날짜 
    SECTION : politics(정치), national(사회), international(국제), culture(문화), index(경제) 중 하나 
    retrun : all_headlines (52주간의 헤드라인이 주별로 저장된 리스트)
    """
    
    if START_WEEK == '시작 주 날짜':
        print("시작 주 날짜 바꿔주세요.")
    else : 
    
        SITE = 'chosunbiz' if SECTION == 'index' else 'www' 

        URL = f"http://news.chosun.com/ranking/list.html?type=&site={SITE}&scode={SECTION}&term=week&date={START_WEEK}"

        # 브라우저 열고, URL로 이동  
        driver = webdriver.Chrome("C:\chrome\chromedriver.exe")
        driver.get(URL)
        sleep(1)

        # 파싱
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # 52주의 모든 헤드라인을 저장할 리스트
        all_headlines = []

        for _ in range(52) : 
            # 태그 안의 콘텐츠 가져오기 
            RANKING_LIST = ["TOPTITLE" + str(n) for n in range(0,30)]
            tags = soup.find_all(True, {"id":RANKING_LIST})

            # 다듬기 
            headlines = [t.getText().strip() for t in tags]
            all_headlines.append(headlines)

            # 다음 주로 이동
            next_button = driver.find_element_by_xpath("//*[@id='btn_next_id']")
            next_button.click() # 클릭
            sleep(1)

        driver.close()

        return all_headlines

# ==============================
# MAIN 
# ==============================

SECTIONS = ['politics', 'national', 'international', 'culture', 'index']
SECTION_HEADLINES = {}

# scrap_chosun 함수에 시작 주만 바꿔주세요 
# 혜민 : scrap_chosun(s, '20170601') 
# 지윤 : scrap_chosun(s, '20180601')

for s in SECTIONS : 
    SECTION_HEADLINES[s] = scrap_chosun(s, "20170601")

with open("chosun_heads.data", "w", encoding = "utf-8") as f : 
    f.write(str(SECTION_HEADLINES))

print("끝")