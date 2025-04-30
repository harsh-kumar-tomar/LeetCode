from typing import List
import math



class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if self.count_digits(num)%2 == 0:
                count += 1
        
        return count
    
    def count_digits(self,n):
        count = 0
        while n != 0:
            n = n // 10
            count += 1
        
        return count

a = Solution().findNumbers(nums = [12,345,2,6,7896])
print(a)