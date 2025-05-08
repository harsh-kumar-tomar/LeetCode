import math
limit = 10**9

N , M = map(int,input().split())
num = 0
i = 0
while i <= M and num <= limit :
    num += math.pow(N,i)
    i += 1

if num <= limit:
    print(int(num))
else:
    print('inf')