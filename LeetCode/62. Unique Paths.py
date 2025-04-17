class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        return self.util(0,0,m,n,dp)
    
    def util(self,currentX: int, currentY: int, m, n, dp):
        
        if currentX == m-1 and currentY == n-1:
            return 1

        if currentX >= m or currentY >= n :
            return 0

        if (currentX,currentY) in dp:
            return dp[currentX,currentY]
        
        a = self.util(currentX+1,currentY,m,n,dp)
        b = self.util(currentX,currentY+1,m,n,dp)

        dp[currentX,currentY] = a+b
        return dp[currentX,currentY]


a = Solution().uniquePaths(3,7)
print(a)

"""
BACKTRACKING
it is a backtracking solution , because here we are trying all possible ways at each stage .
so for any stage i am checking wether i can go Right or Down , if i can i go there .
once reaching the destination i am incraesing the count . 
this code be modified a little bit to track the path , but this is not required in this prob.
"""

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         ls = [0]
#         self.util(1,1,m,n,ls)
#         return ls[0]
    
#     def util(self,currentX: int, currentY: int, m, n, ls):
#         if currentX == n and currentY == m:
#             ls[0] += 1
#             return True

#         if currentX + 1 <= n:
#             self.util(currentX + 1, currentY, m, n, ls)

#         if currentY + 1 <= m:
#             self.util(currentX, currentY + 1, m, n, ls)