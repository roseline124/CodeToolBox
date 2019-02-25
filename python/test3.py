import time

start = time.time()

a = 10
b = 10

i = 0
for i in range(a) :
    for j in range(b) :
        print('*', end='')
    print('\n', end='')
    i+=1


end = time.time()

print(round(end-start,3))