from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left+right)//2
            
            day = self.traverse(mid,weights)

            if day <= days:
                right = mid 
            else:
                left = mid + 1
            
        return left

    def traverse(self,ship_weight:int,weights:List[int]):
        count = 0
        n = len(weights)
        curr_ship_weight = 0
        i = 0
        
        while i <= n:
            
            if i == n :
                count += 1 if curr_ship_weight != 0 else 0 
                break

            if curr_ship_weight + weights[i] > ship_weight:
                count += 1
                curr_ship_weight = weights[i]
            else:
                curr_ship_weight += weights[i]
            
            i += 1
        return count
    
a = Solution().shipWithinDays(weights = [1,2,3,1,1], days = 4)
print(a)

"""
we are traversing the arr from max(arr) ..... sum(arr)
"""