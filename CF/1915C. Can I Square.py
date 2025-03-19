import math

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    s = sum(arr)
    side_of_square = int(math.sqrt(s))
    print("YES") if side_of_square*side_of_square == s else print("NO")
