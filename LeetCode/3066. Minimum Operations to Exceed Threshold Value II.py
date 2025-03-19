import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = 0
        heapq.heapify(nums)

        while len(nums) >= 2 and nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)

            operation = min(a, b) * 2 + max(a, b)
            r += 1
            heapq.heappush(nums, operation)

        return r
