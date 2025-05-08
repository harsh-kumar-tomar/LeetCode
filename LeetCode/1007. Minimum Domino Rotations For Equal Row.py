from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        
        
        top_hash_map = {}
        for i in tops:
            top_hash_map[i] = top_hash_map.get(i,0)+1
        
        top_key = max(top_hash_map,key=top_hash_map.get)
        top_val = top_hash_map[top_key]
    
        bottom_hash_map = {}
        for i in bottoms:
            bottom_hash_map[i] = bottom_hash_map.get(i,0)+1
        
        bottom_key = max(bottom_hash_map,key=bottom_hash_map.get)
        bottom_val = bottom_hash_map[bottom_key]

        if top_val >= bottom_val :
            if bottom_hash_map[top_key] + top_val >= n:
                return n - top_val

        if top_hash_map[bottom_key] + bottom_val >= n:
            return n - bottom_val   
            
        return -1

a = Solution().minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4])
print(a)