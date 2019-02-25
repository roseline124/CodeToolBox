import random

#두구두구, 순서 정하는 야바위 게임~
def cup_and_balls(times, *args) :

    balls = list(args) 
    random.shuffle(balls)

    while len(balls) < times :
        balls.extend(balls)

    result = dict(zip(range(1, times+1), balls))
    print(result)


cup_and_balls(10, '월', '화', '수', '목', '금'  )

