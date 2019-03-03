import time

#1초 세기 
def count_1second() :
    print('current :', time.time())
    time.sleep(1)
    print('after 1 second :', time.time())

count_1second()
