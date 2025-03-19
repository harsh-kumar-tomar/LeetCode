"""
Link: https://leetcode.com/problems/maximum-score-after-splitting-a-string
Difficulty: Easy
Space Complexity: O(n)
Time Complexity: O(n)

Question

1422. Maximum Score After Splitting a String
Solved
Easy
Topics
Companies
Hint
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.



Example 1:

Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3


Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        count_ones = []
        count_zero = []

        prev_one = 0
        prev_zero = 0

        max_sum = float('-inf')

        for char in s:
            temp = int(char)
            if temp == 1:
                prev_one += 1
            count_ones.append(prev_one)

            if temp == 0:
                prev_zero += 1
            count_zero.append(prev_zero)


        for i in range(n-1):
            left = count_zero[i]
            right = prev_one - count_ones[i]

            max_sum = max(max_sum,left+right)


        return max_sum

    # version 2
    # removed counting of presum zero
    def maxScore2(self, s: str) -> int:
        n = len(s)
        count_ones = []
        prev_one = 0
        count_zero = 0
        max_sum = float('-inf')

        for char in s:
            if char == "1":
                prev_one += 1
            count_ones.append(prev_one)

        for index,value in  enumerate(s):
            if value == "0":
                count_zero += 1

            left = count_zero
            right = prev_one - count_ones[index]
            max_sum = max(max_sum,left+right)

        return max_sum







a = Solution().maxScore2("011101")
print(a)
