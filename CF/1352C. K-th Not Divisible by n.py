test = int(input())

for _ in range(test):
    n,k = map(int,input().split())

    el = 1
    count = 0
    while True:
        if el % n != 0:
            count += 1

        if count == k:
            print(el)
            break
        
        el += 1