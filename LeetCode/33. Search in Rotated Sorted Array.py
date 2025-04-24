from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[left] < nums[mid]:
                if nums[left] <=  target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return left if nums[left] == target else -1
    
a = Solution().search(nums = [4,5,6,7,0,1,2], target = 8)
print(a)