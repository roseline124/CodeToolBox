import random

class Dice :

    def __init__(self, sides) : 
        self._sides =  sides
        self._top = random.randint(1, self._sides) #randrange는 stop 미만, randint는 stop 포함

    def top(self) :
        return self._top

    def roll(self) :
        self._top = random.randint(1, self._sides)
        return self._top

dice_4 = Dice(4)      # 사면체 주사위 생성
print('사면체 주사위 테스트 ----')
print('처음 나온 면:', dice_4.top())
print('다시 굴리기:', dice_4.roll())
print('다시 굴리기:', dice_4.roll())

dice_100 = Dice(100)  # 백면체 주사위 생성
print('백면체 주사위 테스트 ----')
print('처음 나온 면:', dice_100.top())
print('다시 굴리기:', dice_100.roll())
print('다시 굴리기:', dice_100.roll())

