
count = 0
nums = [5,10,1,5,2]
k = 1

for index ,val in enumerate(nums):

    temp = ((index//2) + 1) if index%2 == 1 else  1
    if temp == k:
        count += val

print(count)