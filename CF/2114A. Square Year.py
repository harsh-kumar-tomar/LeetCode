import math

n = int(input())

for _ in range(n):
    num = int(input())
    temp = math.sqrt(num)

    if temp == int(temp):
        if temp == 0:
            print(0,0)
        else:
            print(int(temp)-1,1)
    else:
        print(-1) 