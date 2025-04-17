from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)    
        hash_map = {}
        count = 0
        
        for i in range(n):
            el = nums[i]
            if el in hash_map:
                for index in hash_map[el]:
                    if (i*index)%k == 0:
                        count += 1 
            
            hash_map.setdefault(el,[]).append(i)
        
        return count 
    

a = Solution().countPairs(nums = [1,2,3,4], k = 1)
print(a)

"""
mistake:
dividing the result with 2 , thinking i am counting same pair mulitple times , 
i could have counted mutiple time if i was resetting the inner loopo again and again to 0 
but as i am setting j always greater than i than double counting is avoided
"""

# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         n = len(nums)    
#         count = 0
        
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i] == nums[j] and (i*j)%k == 0:
#                     count += 1
        
#         return count 