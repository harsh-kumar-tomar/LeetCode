n, k = map(int, input().split())

ls = list(map(int, input().split()))
k -= 1
i = k

if ls[k] < 1:
    while i > -1 and ls[i] < 1:
        i-=1
else:
    while  i < len(ls) and ls[i] == ls[k]:
        i += 1

print(i+1)
