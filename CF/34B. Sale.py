n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
r = 0
for i in range(m):
    if arr[i] < 0:
        r += abs(arr[i])

print(r)