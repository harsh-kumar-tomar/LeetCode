test = int(input())

for _ in range(test):
    n, k, x = map(int, input().split())

    min_sum = k * (k + 1) // 2
    max_sum = k * (2 * n - k + 1) // 2

    if min_sum <= x <= max_sum:
        print("YES")
    else:
        print("NO")
