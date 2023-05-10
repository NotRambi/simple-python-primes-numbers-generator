i = 1
num = 1
flag = 0
Prim = [2]
while i == 1:    
    for x in range(len(Prim)):
        if num % Prim[x] == 0 and num != Prim[x]:
            flag = 1
    if flag == 0:
        print (num)
        if num != 1:
            Prim.append(num)
    flag = 0       
    num = num + 1
