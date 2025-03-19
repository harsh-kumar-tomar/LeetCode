from typing import List
import sys


def rob(nums: List[int]) -> int:
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

    print(dp)

    return dp[n - 1]


a = rob(nums = [2,7,9,3,1])
print(a)

#
# def rob(self, nums: List[int]) -> int:
#     count = [-1]
#     sum = 0
#     self.ro(nums, len(nums), count, sum, True)
#
#     return count[0]
#
#
# def ro(self, nums, n, count, sum, flag):
#     if n == 0:
#         if count[0] < sum:
#             count[0] = sum
#         return
#
#     # print(sum)
#     if flag:
#         self.ro(nums, n - 1, count, sum + nums[n - 1], False)
#         self.ro(nums, n - 1, count, sum, True)
#     else:
#         self.ro(nums, n - 1, count, sum, True)
#
#
#
#
