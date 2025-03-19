from typing import List


def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    diff_arr = [0]*(n+1)

    # populating diff arr
    for query in queries:
        l,r = query
        diff_arr[l] -= 1
        diff_arr[r+1] += 1

    # taking prefix sum
    for i in range(1,n+1):
        diff_arr[i] += diff_arr[i-1]

    # applying in nums arr
    for i in range(n):
        nums[i] = max(0,nums[i]+diff_arr[i])


    return True if sum(nums) == 0 else False





a = isZeroArray( nums = [1,0,1], queries = [[0,2]])
print(a)
