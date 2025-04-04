from typing import *

path = "/Combination"

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = [i for i in nums]
        nums.sort()  # Sorting is required to handle duplicates correctly
        used = [False] * len(nums)
        r = []
        self.dfs(used, nums, [], r)
        return r

    def dfs(self, used: List[bool], nums: List[int], tempList: List[int], r: List[List[int]]):
        if len(tempList) == len(nums):  # When the permutation is complete
            r.append(tempList.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue  # Skip duplicates if the previous identical number was not used

            used[i] = True
            tempList.append(nums[i])
            self.dfs(used, nums, tempList, r)
            used[i] = False
            tempList.pop()


a = Solution().permuteUnique("AABAA")
print(a)
