from typing import List
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash_map = {}
        n = len(answers)
        count = 0

        for i in range(n):
            key = answers[i]
            hash_map[key] = hash_map.get(key,0) + 1
        
        for key,val in hash_map.items():
            count += math.ceil(val/(key+1))*(key+1)
        
        return count
    
