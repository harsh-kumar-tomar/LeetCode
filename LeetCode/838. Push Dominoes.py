from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        right = deque()
        left = deque()
        n = len(dominoes)
        r = []

        temp_index = float('-inf')
        for i in range(n):
            if dominoes[i] == "R":
                temp_index = i
            right.append(temp_index)
        
        temp_index = float('inf')
        for i in range(n-1,-1,-1):
            if dominoes[i] == "L":
                temp_index = i
            left.appendleft(temp_index)
        
        print(right)
        print(left)
        ".L.R...LR..L.."
        for i in range(n):
            r_dis = i-right[i]
            l_dis = left[i]-i
            
            if r_dis == l_dis:
                r.append(".")
            elif r_dis > l_dis:
                r.append("L")
            else:
                r.append("R")
        
        return "".join(r)
        
    
a = Solution().pushDominoes(dominoes = ".L.R...LR..L..")
print(a)