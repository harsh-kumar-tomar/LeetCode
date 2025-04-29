from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count_max = 0
        count_subarr = 0
        max_el = max(nums)
        index_arr = []
        end = 0
        n = len(nums)

        while end < n:
            
            if nums[end] == max_el :
                count_max += 1
                index_arr.append(end)

            if count_max >= k:
                count_subarr += (index_arr[-k]+1)

            end += 1
        
        return count_subarr 

a = Solution().countSubarrays(nums  = [1,3,2,3,3] , k = 2)
print(a)

"""
advice 
be aware of double counting . 
so while solving  this prob i was counting for both the side for left as well as right .

for ex
arr = 1 , 3, 2, 3, 3
k = 2

Mistake
so the sub arr that satisfies the condition is 3,2,3 
so i was counting for 
3,2,3 + 1,3,2,3 + {1,3,2,3,3} + (3,2,3,3) 

another another subarray is 3,3
so i was counting for 
{1,3,2,3,3} + (3,2,3,3) + ,2,3,3 + 3,3
{} , () are double counting 

tip 
always count either to the left or to the right not both at the same time .
"""