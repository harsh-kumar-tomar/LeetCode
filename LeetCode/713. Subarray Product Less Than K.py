from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = end = 0
        total_pro = 1
        total_subarr = 0
        n = len(nums)

        while end < n :
            total_pro *= nums[end]

            while start <= end and total_pro >= k:
                total_pro = total_pro // nums[start]
                start += 1
            
            total_subarr += end - start + 1

            end += 1
        
        return total_subarr



a = Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
print(a)