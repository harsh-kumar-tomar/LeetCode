n,m = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
big_num = float('-inf')
small_num = float('inf')

for i in range(n):
    big_num = max(big_num,i)
    small_num = min(small_num,i)

diff = (big_num-small_num)

for i in range(n,len(arr)):
    if i > big_num:
        big_num = max(big_num,i)
    if i < small_num:
        small_num = min(small_num,i)
    diff = min(diff,big_num-small_num)

print(diff)
