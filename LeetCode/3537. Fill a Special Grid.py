from typing import List
import math

class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 2**n
        val = [0]
        matrix = [[0]*size for i in range(size) ]
        self.recursion(0,size,0,size,size,val,matrix)
        return matrix
    
    def recursion(self,row_st , row_end , col_st , col_end , n , val,matrix):

        if n == 1:
            matrix[row_st][col_st] = val[0]
            val[0] += 1
            return
            
        row_mid = row_st + n//2
        col_mid = col_st + n //2

        self.recursion(row_st, row_mid , col_mid , col_end , n//2 , val , matrix)
        self.recursion(row_mid, row_end , col_mid , col_end , n//2 , val , matrix)
        self.recursion(row_mid, row_end , col_st , col_mid , n//2 , val , matrix)
        self.recursion(row_st,row_mid , col_st , col_mid , n//2 , val , matrix)




a = Solution().specialGrid(2)
print(a)

"""
advice
pls dont confuse between row , column
"""