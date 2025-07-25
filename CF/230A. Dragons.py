s , n = map(int,input().split())
arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

arr.sort(key=lambda x: x[0])

for i,j in arr:
    if s > i :
        s += j
    else:
        print("NO")
        break
else:
    print("YES")