test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))

    print((6*(9-n)*(9-n+1))//2)