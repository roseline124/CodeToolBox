def read_file() :

    try : 
        print('파일 이름을 입력하시오: ', end='')
        filename = input()

        # filename 파일 열기
        with open(filename) as f:
            # 파일의 내용을 읽어 화면에 출력
            print(f.read())

    except FileNotFoundError: 
        print("아이고, 파일이 없는데요?\n(en: There is no such file)")

read_file()