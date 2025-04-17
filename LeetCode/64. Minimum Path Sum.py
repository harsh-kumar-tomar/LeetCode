from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def min_points(x,y):

            if x == m- 1 and y == n- 1:
                return grid[-1][-1] 

            if x >= m or y >= n:
                return float('inf')

            if (x,y) in dp:
                return dp[x,y]

            a = min_points(x+1,y)
            b = min_points(x,y+1)

            dp[x,y] = grid[x][y] + min(a,b) 


            return dp[x,y]

        dp = {}   
        
        m , n = len(grid) , len(grid[0])
        return min_points(0,0)

