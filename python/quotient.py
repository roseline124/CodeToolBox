"""
연습문제 11-1 몫 구하기

몫 연산자 없이 몫을 구하려면 어떻게 해야 할까?

10을 6으로 나눈 몫을 구하는 프로그램을 
몫 연산자를 사용하지 않고 작성해 보아라.
"""

def get_quotient(molecule, denominator) :

    quotient = 0 

    while molecule > 0 :
        molecule -= denominator
        quotient += 1

        if molecule - denominator < 0 :
            break 

    return quotient

print(get_quotient(13, 6))