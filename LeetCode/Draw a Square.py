test = int(input())

for _ in range(test):
    arr = list(map(int, input().split()))
    l, r, d, u = arr

    print("Yes") if l == r == d == u else print("No")
