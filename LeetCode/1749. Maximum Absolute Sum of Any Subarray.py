from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')

        # for calc max sum
        curr_sum = 0
        for i in nums:
            curr_sum += i
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0 :
                curr_sum = 0


        # for calc min sum
        curr_sum = 0
        for i in nums:
            curr_sum += i
            min_sum = min(min_sum,curr_sum)
            if curr_sum > 0:
                curr_sum = 0
            

        return max(max_sum,-1*min_sum)

a = Solution().maxAbsoluteSum(nums =[-1,-1])
print(a)