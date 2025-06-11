import math

n , k = map(int,input().split())

odd_num = math.ceil(n/2)
even_num = n//2

if k <= odd_num:
    print((2*k)-1)
else:
    print((k-odd_num)*2)