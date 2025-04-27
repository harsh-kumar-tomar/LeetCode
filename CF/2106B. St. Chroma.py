test = int(input())

for _ in range(test):
    n,x = map(int,input().split())
    arr = [i  for i in range(n) if i != x ]
    if len(arr) < n : arr.append(x)
    print(*arr)