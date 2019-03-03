"""
연습문제 11-7 텍스트 파일 복사

파일 경로를 나타내는 문자열 두 개를 인자로 전달받아, 
텍스트 파일을 복사하는 함수cp(src, dst)를 작성하라. 

예를 들어, 이 함수를 다음과 같이 호출하면 original.txt 
파일을 clone.txt 파일로 복사한다.
"""

def cp(src, dst) :
    try : 
        with open(src, 'r', encoding='utf-8') as f : 
            data = f.read()

        with open(dst, 'w', encoding='utf-8') as f : 
            f.write(data)

    except FileNotFoundError : 
        print("파일이 없는데요?")

cp('original.txt', 'clone.txt')