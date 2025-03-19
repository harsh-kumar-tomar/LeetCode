import math

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    even_idx = -1
    odd_idx = -1

    for index, val in enumerate(arr):
        if index % 2 == 0 and val > even_idx:
            even_idx = val

        if index % 2 == 1 and val > odd_idx:
            odd_idx = val

    print(max(even_idx + math.ceil(len(arr) / 2), odd_idx + math.floor(len(arr) / 2)))
