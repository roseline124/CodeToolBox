import time

start = time.time()

a = 1000
b = 1000

answer = ('*'*a +'\n')*b
print(answer)

end = time.time()

print(round(end-start,3))