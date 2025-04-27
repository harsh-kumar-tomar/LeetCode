from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        start = 0
        end = 0
        count_subarr = 0
        count_perfect_el = 0

        for end in range(n):
            
            if nums[end] % modulo == k:
                count_perfect_el += 1
            
            if count_perfect_el % modulo == k:
                count_subarr += n - end
                
        
        return count_subarr

a = Solution().countInterestingSubarrays( nums = [3,1,9,6], modulo = 3, k = 0)
print(a)