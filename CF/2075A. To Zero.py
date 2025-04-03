
test = int(input())

for _ in range(test):
    operation = 0
    n , k = map(int,input().split())

    while n != 0:

        if n <= k:
            n = n -k
            operation += 1
            break

        if n % 2 == 0:
            operation += n//(k-1)
            n = n %(k-1)
        else:
            n = n - k
            operation += 1

    print(operation)