from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        end = 0
        max_product = float('-inf')
        temp_product = 1
        n = len(nums)

        while end < n:
            
            if nums[end] == 0:
                temp_product = 0
            elif temp_product <= 0:
                temp_product = nums[end]
            else:
                temp_product *= nums[end]

            max_product = max(max_product,temp_product)
            end += 1
        
        return max_product


a = Solution().maxProduct(nums =[2,3,-2,4])
print(a)