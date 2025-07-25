n = (input())
l = len(n)

if int(n) >= 0:
    print(n)
else:
    if n[-1] > n[-2]:
        print(int(n[0:len(n)-1]))
    else:
        print(int(n[0:len(n)-2]+n[-1]))