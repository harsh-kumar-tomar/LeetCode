def lucky(i):
    while i != 0:
        rem = i % 10
        if rem != 4 and rem != 7:
            return False
        i = i//10
    return True


n = int(input())

for i in range(1,n+1):
    if lucky(i):
        if n%i == 0 :
            print("YES")
            break
else:
    print("NO")