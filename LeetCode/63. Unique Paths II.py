from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def unique_path(x,y):

            if x >= m or y>=n or obstacleGrid[x][y] == 1:
                return 0
            
            if x == m-1 and y == n -1:
                return 1
            
            if (x,y) in dp:
                return dp[x,y]

            dp[x,y] = unique_path(x+1,y) + unique_path(x,y+1) 
            return dp[x,y]


        dp = {}
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        return unique_path(0,0)