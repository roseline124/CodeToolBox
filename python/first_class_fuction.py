"""
First Class Function
함수 자체를 인자 (argument) 로써 다른 함수에 전달하거나 
다른 함수의 결과값으로 리턴 할수도 있고, 
함수를 변수에 할당하거나 데이터 구조안에 저장할 수 있는 함수
"""

# -*- coding: utf-8 -*-

def square(x):
    return x * x

print(square(5))

f = square

print(square)
print(f)