"""
Link: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Space Complexity: O(n)
Time Complexity: O(n)

Question:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = [intervals[0]]
        j = 1

        intervals.sort(key=lambda x: x[0])

        while j < len(intervals):
            if r[-1][1] >= intervals[j][0]:
                r[-1][1] = max(r[-1][1], intervals[j][1])
            else:
                r.append(intervals[j])
            j += 1

        return r


a = Solution().merge([[1, 4], [0, 4]])

print(a)


# old code
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        ans = []
        pointer = -1

        for interval in intervals:

            if pointer == -1:
                pointer = 0
                ans.append(interval)
            # 1,4    4,5
            if ans[pointer][1] >= interval[0]:
                ans[pointer] = [ans[pointer][0], max(ans[pointer][1], interval[1])]
            else:
                ans.append(interval)
                pointer += 1

        return (ans)
