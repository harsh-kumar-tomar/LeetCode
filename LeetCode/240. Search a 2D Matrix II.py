from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        y = 0
        x = len(matrix[0]) - 1
  

        while x >= 0 and y < len(matrix):
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                x -= 1
            else:
                y += 1
        
        return False
'''
all row are independent , binary seach would work (
first to find appro. x , than
first to find appro. y
)

but binary seach wont work in this case because row and coloumn are independent .
so it is kind of optimized linear search .

we can start from  top right or bottom left .
we have also decreased the search space by starting from the top left as 
there is no where to go , to increase the value . 
'''