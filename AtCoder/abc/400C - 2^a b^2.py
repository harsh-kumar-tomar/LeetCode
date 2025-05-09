import math

n = int(input())
count = 0

if n >= 2:
    count += math.isqrt(n//2)

if n>= 4:
    count += math.isqrt(n//4)



print(count)


"""
n = int(input())

count = 0
b = 1
s = set()

while b <= math.isqrt(n):
    a = 1
    while b*b*math.pow(2,a) <= n:
        s.add(b*b*math.pow(2,a))
        a += 1
    b += 1

print(len(s))
"""
