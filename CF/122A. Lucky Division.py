n = int(input())

if n%4 == 0 or n%7 == 0:
    print("YES")
else:
    n = str(n)
    flag = True
    for char in n:
        if char != "4" and char != "7":
            flag = False
            break
    print("YES") if flag else print("NO") 