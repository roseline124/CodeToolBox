import time

start = time.time()

a = '1000'
b = '1000'

a = int(a)
b = int(b)
i = 0

while i < b :
    print('*'*a)
    i += 1

end = time.time()

print(round(end-start,3))