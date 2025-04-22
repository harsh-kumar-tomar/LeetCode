from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        arr = [1]

        for diff in differences:
            el = arr[-1]+diff
            arr.append(el)

        
        min_el = min(arr)
        max_el = max(arr)
        a = list(range(lower-min_el,upper-max_el+1))
        return len(a)



a = Solution().numberOfArrays(differences = [4,-7,2], lower = 3, upper = 6)
print(a)