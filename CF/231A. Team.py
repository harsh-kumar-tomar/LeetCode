
n = int(input())
count = 0
for i in range(n):
    ls = list(map(int,input().split()))
    s = sum(ls)
    count += 1 if s >= 2 else 0

print(count)