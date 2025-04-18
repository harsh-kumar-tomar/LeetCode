import sys
data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int,data[1:]))

s = sum(arr)
total_sum = n*(n+1)//2

print(total_sum-s)