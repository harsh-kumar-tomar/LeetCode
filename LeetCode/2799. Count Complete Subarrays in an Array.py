from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = 0
        distict_el = len(set(nums))
        hash_map = {}
        count_subarray = 0

        for end in range(n):

            el = nums[end]
            
            hash_map[el] = hash_map.get(el,0) + 1

            if len(hash_map) == distict_el:
                count_subarray += n - end 
                
                while len(hash_map) == distict_el:
                    temp_el = nums[start]
                    hash_map[temp_el] = hash_map.get(temp_el) - 1
                    
                    if hash_map[temp_el] == 0:
                        hash_map.pop(temp_el)
                    else:
                        count_subarray += n - end 
                    
                    start += 1



        return count_subarray
    
a = Solution().countCompleteSubarrays(  nums = [5,5,5,5])
print(a)