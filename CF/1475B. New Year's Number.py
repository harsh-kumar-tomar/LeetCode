
test = int(input())

for _ in range(test):
    n = int(input())

    x = n%2020
    y = (n-x)//2020 - x

    if x >= 0 and y>=0:
        print("YES")
    else:
        print("NO")