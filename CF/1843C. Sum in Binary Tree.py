test = int(input())

for _ in range(test):
    n = int(input())
    r = n

    while n!=0:
        r += n//2
        n = n // 2
    
    print(r)