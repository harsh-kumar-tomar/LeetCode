from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(self.rob(nums[:-1]), self.rob(nums[1:]))

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [-1] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            take = nums[i] + dp[i - 2]
            leave = dp[i - 1]
            dp[i] = max(take, leave)

        return dp[n - 1]

a = Solution().rob(nums = [1,2,3])
print(a)