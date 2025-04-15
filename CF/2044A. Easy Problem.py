
test = int(input())

for _ in range(test):
    n = int(input())
    count = 0

    for i in range(1,n):
        if abs(n-i) < n:
            count+= 1

    print(count)

