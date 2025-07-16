from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        low = 0
        high = nums[-1]-nums[0]
        ans = -1

        while low <= high :
            mid = (high + low)//2

            if self.is_good(nums,p,mid):
                ans = mid
                high =  mid -1
            else:
                low = mid + 1
        
        return ans


    def is_good(self,nums,p,v):
        n = len(nums)
        i = 1
        count = 0

        while i < n:
            if nums[i] - nums[i-1] <= v:
                count += 1
                i += 2
            else:
                i += 1

        return count >= p