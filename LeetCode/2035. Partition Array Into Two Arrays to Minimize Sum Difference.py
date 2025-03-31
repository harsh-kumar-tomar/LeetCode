import math
from typing import List


def minimumDifference(nums: List[int]) -> int:
    n = len(nums)

    total_sum = sum(nums)

    subset1 = []
    subset2 = []
    recursion(0, n // 2, nums,0,subset1)
    recursion(n // 2 , n, nums,0,subset2)

    subset1.sort()




def recursion(current_pos, end_pos, nums, temp_sum, subset):
    if current_pos > end_pos:
        return

    if current_pos == end_pos:
        subset.append(temp_sum)
        return

    recursion(current_pos + 1, end_pos, nums, temp_sum + nums[current_pos], subset)
    recursion(current_pos + 1, end_pos, nums, temp_sum, subset)


a = minimumDifference( nums = [3,9,7,3])
print(a)








"""

def minimumDifference(nums: List[int]) -> int:
    ls = [10000]
    recursion(nums,0,len(nums)//2,ls,0,sum(nums))
    return ls[0]

def recursion(nums,current_pos:int,choice:int,min_diff,sum1,total_sum):

    if choice == 0:
        sum2 = total_sum-sum1
        min_diff[0] = min(min_diff[0], abs(sum1 - sum2 ))
        return

    if current_pos >= len(nums) :
        return

    if choice > 0:
        #take the element , increase sum1
        recursion(nums,current_pos+1,choice-1,min_diff,sum1+nums[current_pos],total_sum)
        #leave element
        recursion(nums,current_pos+1,choice,min_diff,sum1,total_sum)

"""
