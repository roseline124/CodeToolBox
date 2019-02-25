import time

start = time.time()

a = 100
b = 100
i = 0
while i < a :
    j=0
    while j < b :
        print('*', end='')
        j+=1
    print('\n')
    i+=1

end = time.time()
print(round(end-start,3))