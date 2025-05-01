
n = int(input())
arr = list(map(int,input().split()))
total_sum = sum(arr)
half_sum = total_sum // 2
arr.sort()

for i in range(n,-1,-1):
    if half_sum>= i:
        half_sum -= i

print(half_sum + total_sum//2)
    