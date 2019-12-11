import time

sum = 0
num = 0
t1= time.time()


for num in range(0,10000000):
    sum += num
t2 = time.time()

print(sum)
print(t2 - t1)