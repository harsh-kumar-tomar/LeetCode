import math
test = int(input())

for _ in range(test):
    x,y,k = map(int,input().split())
    if x == 0  and y == 0:
        print(0)
    else:
        print(2*(math.ceil(y/k))) if math.ceil(y/k) >= math.ceil(x/k) else print( (2*math.ceil(x/k)) -1 )