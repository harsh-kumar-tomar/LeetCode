test = int(input())

for _ in range(test):
    n = int(input())

    while n != 1:
        if n%2 == 0:
            n = n //2
        else:
            break
    
    print("YES") if n != 1 else print("NO")