k , r = map(int,input().split())

num = 1

while (k*num)%10 != r and (k*num)%10 != 0 :
    num += 1

print(num)
import math
math