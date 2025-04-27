test = int(input())

for _ in range(test):
    n = int(input())
    s = input()

    total_ones = 0
    count_ones = 0

    for char in s:
        if char == "1":
            total_ones += 1

    for i in range(n):
        if s[i] == "1":
            count_ones += total_ones - 1
        else:
            count_ones += total_ones + 1
    
    print(count_ones)