test = int(input())

for _ in range(test):
    n = int(input())

    cows = n // 4
    n = n % 4
    chicken = n // 2

    print(cows+chicken)