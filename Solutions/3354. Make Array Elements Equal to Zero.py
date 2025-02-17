from typing import List

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        count = 0

        for index, value in enumerate(nums):
            if value == 0:
                if self.motion(nums.copy(), index, 1):
                    count += 1
                if self.motion(nums.copy(), index, -1):
                    count += 1

        return count

    def motion(self, nums: List[int], index: int, direction: int) -> bool:
        curr = index
        n = len(nums) - 1
        tempSum = sum(nums)

        while 0 <= curr <= n:
            if tempSum == 0:
                return True

            if nums[curr] > 0:
                nums[curr] -= 1
                tempSum -= 1
                direction = (-1 if direction == 1 else 1)

            curr += direction

        return False
