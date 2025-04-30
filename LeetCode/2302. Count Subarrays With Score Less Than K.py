from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = end = 0
        total_sum = 0
        total_subarr = 0
        n = len(nums)

        while end < n:
            total_sum += nums[end]

            while start <= end and  total_sum*(end - start + 1) >= k:
                total_sum -= nums[start]
                start += 1

            total_subarr += end - start + 1 


            end += 1

        return total_subarr
        
a = Solution().countSubarrays(nums = [2,1,4,3,5], k = 10)
print(a)