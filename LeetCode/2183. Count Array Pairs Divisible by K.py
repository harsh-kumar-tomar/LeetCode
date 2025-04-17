from typing import List
import math
class Solution:
    def countPairs(self,nums: List[int], k: int) -> int:
        n = len(nums)
        el_divisible = 0
        el_not_divisible = 0 

        for i in range(n):
            if nums[i] % k == 0:
                el_divisible += 1
            else:
                el_not_divisible += 1
    
        return (el_divisible*el_not_divisible) +  math.comb(el_divisible,2)


a = Solution().countPairs(nums = [1,2,3,4], k = 5)
print(a)


"""
Brute Force
"""


# class Solution:
#     def countPairs(self,nums: List[int], k: int) -> int:
#         n = len(nums)
#         count = 0

#         for i in range(n):
#             for j in range(i+1,n):
#                 if (nums[i]*nums[j]) % k == 0:
#                     count += 1

#         return count 