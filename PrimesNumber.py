import math
import time

Prim = [2]
num = 3
flag = 0
t0 = time.time()
t1 = time.time()

while True:
        t1 = time.time()
        r = math.floor(math.sqrt(num))+ 1
        for x in range(len(Prim)):
            if Prim[x] > r:
                break
            if num % Prim[x] == 0 and num != Prim[x]:
                flag = 1
                break
        if flag == 0:
            if t1 - t0 > 60:
                print('last Prime number find: ',num,' number of Prime calculated: ',len(Prim))
                t0 = t1
            Prim.append(num)
        flag = 0       
        num += 1
