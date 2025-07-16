n , k = map(int,input().split())
x,a,b,c = map(int,input().split())

# generating arr
arr = [x]
for i in range(1,n):
    arr.append((a*arr[-1]+b)%c)

# calc window sum
s = 0
for i in range(k):
    s += arr[i]

# calc after window sum
ans = s
for i in range(k,len(arr)):
    s -= arr[i-k]
    s += arr[i]
    ans = ans^s

print(ans)

