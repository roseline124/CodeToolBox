#request.urlopen() 함수 사용하기
#urlretrieve()함수는 파일로 곧바로 저장하지만 urlopen()은 일단 메모리에 로딩. 이후, 파일로 저장할 건지 말지 결정 가능
#urlopen은 retrieve와 달리 데이터를 정제해서 다운받을 수 있다.

import urllib.request

url = "https://t1.daumcdn.net/daumtop_chanel/op/20181008012324934.png"
imgName2 = "C:/Users/roseline/pyscrap/daum2.png"

mem = urllib.request.urlopen(url).read()
#urlopen으로 url 위치 지정 후, read함수로 읽어와야 한다.
#mem이라는 변수에 이미지를 불러오는 것.

#파일로 저장하는 과정
#f = open("a.txt", "w")
#f.write("테스트로 파일에 내용을 적는다.")
#f.close()

#위의 과정을 with 문으로 간단하게 표현 -> close 문을 사용할 필요 없다.

#with open("a.txt", "w") as f:
#f.write("테스트로 파일에 내용을 적는다.")

with open(imgName2, mode = "wb" ) as f:
#이미지 파일은 bin형태(이진수 형태)로 저장되어 있다.
# w는 쓰기 모드, b는 바이너리 모드(이미지)

    f.write(mem)

print("이미지 다운로드 완료")
