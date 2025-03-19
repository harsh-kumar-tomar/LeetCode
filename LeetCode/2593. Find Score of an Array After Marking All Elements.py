"""
Link: https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements
Difficulty: Medium
Space Complexity: O(n)
Time Complexity: O(nlogn)

Question

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.



Example 1:

Input: nums = [2,1,3,4,5,2]

Output: 7

Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.
Example 2:

Input: nums = [2,3,5,1,3,2]

Output: 5

Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.


Constraints:

1 <= nums.length <= 105

1 <= nums[i] <= 106
"""

import heapq
import math
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap = []
        sum = 0
        n = len(nums)

        for index, value in enumerate(nums):
            temp = [value, index]
            heapq.heappush(min_heap, temp)

        while True:
            index = self.findSmallestNumberIndex(min_heap)
            if index == -1:
                break

            if nums[index] == float('inf'):
                continue

            sum += nums[index]
            nums[index] = -nums[index]

            if 0 < index < n - 1:
                nums[index + 1] = float('inf')
                nums[index - 1] = float('inf')
            elif index == 0:
                nums[index + 1] = float('inf')
            else:
                nums[index - 1] = float('inf')

        print(sum)

    def findSmallestNumberIndex(self, min_heap: list[List[int]]) -> int:
        if not min_heap:
            return -1
        else:
            temp = heapq.heappop(min_heap)
            return temp[1]


Solution().findScore(nums = [2,1,3,4,5,2])
