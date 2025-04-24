from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left+right)//2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                right  = mid - 1
        


a = Solution().findMin(nums = [11,13,15,17])
print(a)