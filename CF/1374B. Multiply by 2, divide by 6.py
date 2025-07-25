test = int(input())
for _ in range(test):
    n = int(input())
    
    while n!=1:
        if n%6 == 0:
            n = n //6
        else:
            n = n * 2