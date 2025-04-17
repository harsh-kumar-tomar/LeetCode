from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def unique_path(x,y,count):
            if x >= m or y >= n or x < 0 or y < 0 or grid[x][y] == -1 or grid[x][y] == float('inf'):
                return 0
            
            if (x,y,count) in dp:
                return dp[x,y,count]
            
            if x == flag_x and y == flag_y  :
                return 1 if count == empty_space  else 0


            count += 1

            grid[x][y] = float('inf')
            dp[x,y,count] = unique_path(x+1,y,count) + unique_path(x,y+1,count) + unique_path(x-1,y,count) + unique_path(x,y-1,count)
            grid[x][y] = 0
            
            return dp[x,y,count]  
        
        m , n = len(grid) , len(grid[0])
        origin_x = -1
        origin_y = -1
        flag_x = -1
        flag_y = -1
        empty_space = 1
        dp = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    origin_x , origin_y = i,j
                if grid[i][j] == 2:
                    flag_x,flag_y = i,j
                if grid[i][j] == 0 :
                    empty_space += 1
        
        return unique_path(origin_x,origin_y,0)
    

a = Solution().uniquePathsIII(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]])
print(a)

"""
if x,y == flagx,flagy but count != empty_spaces
mistakely setting the flag_x , flag_y = -1 
"""