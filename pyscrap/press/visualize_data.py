# 형태소 분석 위한 라이브러리 import 
import nltk 
from konlpy.tag import Okt; t = Okt()

# ==============================
# 최빈어 추출 위한 전처리 작업  
# ==============================

with open("chosun_2016.data", "r", encoding='utf-8') as f : 
    # 연도별로 저장했던 헤드라인 파일의 내용을 불러온다. 
    headlines = f.read()

# 텍스트를 의미를 지닌 가장 작은 단위로 쪼개어 리스트로 반환 
# ex) "최선의 노력" -> ["최선", "의", "노력"]
tokens = t.morphs(headlines)

# 불용어 필터링 
# stop_words : 의미 없는 불용어들을 걸러내기 위한 리스트 
stop_words = ["'", '"', ',', '','…', '에', '이', '의', '·', '을', '은', '한', '...',
            '가', ']', '도', '들', '1', '는', '?', '로', '에서', '위', '과', '..', '된','서', '앞', '‘','(', '[',
            '\'…', '.', '2', '수', '세', '를', '지난', '자', "때", "못", '""', '…"', '명',
            '까지', '으로', ")',", '"\'', "',", "'[", '"\\', "\\'", '",' , '\'"', '"…', '\'",',
            '"\',', '대', '와', '우리', '"[', '안', '것', '더', '고', "?", "살", "부터", "오늘", "?',",
            "두", "…'", ')', '왜', 'Why', '하는', '가장', '있는', "대통령", "세계", "운세", "6월", 
            "음력", "한국", "여성조선", "단독", "발견", "할", "받아", "덮", "네", "이번", "'",
            "',",',', '"', ']', "'[", '…', '의', '에', '"\',', '다', '해', '라', '뒤', 
            '기', '적', '만', '’', '…"\',', '하지', '지', '사람',"['", '”', '“',
            '만에', '장', "'\\'", '-', '전', '그', '있다', '고백', '등', '간', '날', "'],", "…',",
            "[],", '[]],', '정치', '사회', '[]],', '[[],', "’'," ,"['[", "경제",
            '’…', '내', '했다', '이유', "국제", "당", "문", "스포츠", "영상", "문화",
            "속보"] 

# 불용어 제외한 단어만 tokens에 다시 저장 
tokens = [word for word in tokens if word not in stop_words]

# tokens를 nltk 텍스트 타입의 객체로 변환. 
txt = nltk.Text(tokens, name='txt')


# ==============================
# 최빈어 워드클라우드 시각화  
# ==============================

from matplotlib import font_manager, rc 
import platform
import matplotlib.pyplot as plt 
# %matplotlib inline # 주피터의 경우 

# 운영체제에 따라 한글 폰트 변경 
path = "C:/Windows/Fonts/malgun.ttf"

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else :
    print('Unknown system. Sooooorry.')

plt.rcParams['axes.unicode_minus'] = False

# 워드클라우드 관련 라이브러리 import 
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# 최빈 단어 TOP 300의 (단어, 빈도수) 쌍으로 이루어진 것들의 리스트 : [('노소영', 572),]
data = txt.vocab().most_common(300)


wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', # 윈도우 운영체제 폰트 경로
                      relative_scaling = 0.5,
                      background_color='white'
                     ).generate_from_frequencies(dict(data))
plt.figure(figsize=(16, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show


