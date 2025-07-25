test = int(input())

for _ in range(test):
    n = int(input())
    
    i = 2
    ans = - 1
    while i < 40:
        if n%(pow(2,i)-1) == 0:
            ans = n//(pow(2,i)-1)
            break
        i += 1

    print(ans)