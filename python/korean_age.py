"""
연습문제 11-6 한국식 나이

세는 나이: 태어난 해를 기준으로 1세, 
해가 바뀔 때마다 바로 한 살 씩 증가

만 나이: 생년월일을 기준으로 0세, 
해가 바뀌고 생일이 지날 때마다 한 살씩 증가
--------------
세는 나이를 반환하는 함수 
counting_age(birth_date)

만 나이를 반환하는 함수 
full_age(birth_date)를 각각 정의해라.
"""

from datetime import date, timedelta

# 세는 나이 
def counting_age(birth_date) :
    age = 1 
    today = date.today()
    y = birth_date[0]

    while y != today.year : 
        age += 1
        y += 1 

    return age

#만 나이
def full_age(birth_date) :
    age = 0 
    today = date.today()
    birth_date = date(birth_date[0], birth_date[1], birth_date[2])

    while (today - birth_date) > timedelta(0) :
        birth_date += timedelta(365)
        if (birth_date.year <= today.year) : #해가 바뀌고 
            if (birth_date.month, birth_date.day) <= (today.month, today.day) : # 생일이 지날 때 
                age += 1

    return age 

birthday = (2000, 1, 24)
print(f'{counting_age(birthday)}세')
print(f'만 {full_age(birthday)}세')
