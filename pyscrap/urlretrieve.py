#urllib : http, ftp를 사용해 데이터를 다운로드할 때 사용하는 라이브러리
#urllib 내의 모듈 중 request 모듈을 사용하고 그 모듈 안에 있는 retrieve()함수 사용
import urllib.request #점으로 모듈을 구분한다.

url = "https://t1.daumcdn.net/daumtop_chanel/op/20181008012324934.png"
imgName = "C:/Users/roseline/pyscrap/daum.png" #위의 긴 주소를 이 경로에 daum.png라는 이름으로 저장

# 이 파이썬 파일을 실행시키면 위의 이미지를 다운받을 수 있다.

urllib.request.urlretrieve(url, imgName) # 변수 : 주소, 저장 경로
print("다운로드 완료")
