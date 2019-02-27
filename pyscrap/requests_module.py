# #request 모듈 메서드
# import requests
# #http에서 사용하는 데이터 전송 방식 : get, post 방식 / 두 방식의 메서드 제공
#
# r = request.get("http://google.com") #get 방식
#
# #post
# formData = {"key1":"value1","key2":"value2"}
# r = requests.post{"http://sample.com", formData}

# 텍스트 데이터 가져오기
import requests
resData = requests.get("http://api.aoikujira.com/time/get.php")

#텍스트 형식으로 추출하기
txt = resData.text

print(txt)

#바이너리 형식으로 추출하기

bin = resData.content #바이너리 데이터 타입의 명칭은 content

print(bin)
