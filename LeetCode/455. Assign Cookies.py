from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                j += 1

        return count
    



a = Solution().findContentChildren(g = [1,2,3], s = [1,1])
print(a)

"""
here we need to assign as much as sweet as possible .
not as much as  greed . 
so greed depends upon sweet
"""