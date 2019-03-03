"""
연습문제 11-5 한글만 남기기

한글을 제외한 모든 문자를 나타내는 정규 표현식 패턴 
not_hangul_pattern을 정의해라. 

그리고 이를 활용해 전달받은 문자열에서 한글만 남겨 
반환하는 함수 hangul_only(string)를 정의해라.
"""

import re

def hangul_only(string) :

    not_hangul_pattern = re.compile(r'[^가-힣]')
    string = re.sub(not_hangul_pattern, '', string)

    return string 

print(hangul_only('I like 파이썬 programming.'))
print(hangul_only('a1가b2나c3다d4라e5마f6바g7사'))