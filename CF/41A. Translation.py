s1 = input()
s2 = input()
n = len(s1)
m = len(s2)

if n != m:
    print("NO")
else:
    i = 0
    j = n -1 
    ok = True

    while i < n and j >= 0:
        if s1[i] != s2[j]:
            ok = False
            break
        i += 1
        j -= 1

    print("YES") if ok else print("NO")