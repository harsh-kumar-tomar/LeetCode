"""
Link: https://leetcode.com/problems/target-sum
Difficulty: Medium
Space Complexity: O(n*s)
Time Complexity: O(n*s) or len(nums)(2*sum(nums)+1)

Question

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1


Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        a = self.path(nums, 0, target, 0, mem)
        return a

    def path(self, nums: List[int], pointer: int, target: int, sum: int, mem) -> int:

        if pointer == len(nums):
            return 1 if sum == target else 0

        if (pointer, sum) in mem:
            return mem[(pointer, sum)]
        else:
            add = self.path(nums, pointer + 1, target, sum + nums[pointer],mem)
            subtract = self.path(nums, pointer + 1, target, sum - nums[pointer],mem)

            mem[(pointer, sum)] = add + subtract
            return mem[(pointer, sum)]


a = Solution().findTargetSumWays(nums=[30, 1, 5, 32, 16, 17, 30, 29, 48, 14, 29, 4, 31, 12, 40, 13, 13, 20, 41, 38],target=9)
print(a)