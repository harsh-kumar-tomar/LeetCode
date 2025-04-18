import sys

data = sys.stdin.read().split()

n = int(data[0])
arr = list(map(int,data[1:]))
moves = 0

for i in range(1,n):
    if arr[i] < arr[i-1]:
        moves += arr[i-1] - arr[i]
        arr[i] = arr[i-1]


print(moves)


"""
mistake : dont forget the assignment part 
"""