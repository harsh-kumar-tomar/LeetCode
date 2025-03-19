n = int(input())

for i in range(n):
    ls = list(map(int, input().split()))
    s = sum(ls)
    flag = False
    for el in ls:
        if s - el == el:
            flag = True
            break
    print("YES") if flag else print("NO")
