"""
Link: https://leetcode.com/problems/is-subsequence
Difficulty: Easy
Space Complexity: O(n)
Time Complexity: O(n)

Question:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

import heapq
import math
from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

        # time limit exceed
        # lcs = self.lcs(s,0,t,0)
        # return True if lcs == len(s) else False

    def lcs(self, s1, p1, s2, p2):

        if len(s1) == p1 or len(s2) == p2:
            return 0

        if s1[p1] == s2[p2]:
            return 1 + self.lcs(s1, p1 + 1, s2, p2 + 1)
        else:
            temp1 = self.lcs(s1, p1 + 1, s2, p2)
            temp2 = self.lcs(s1, p1, s2, p2 + 1)

            return max(temp1, temp2)


a = Solution().isSubsequence("rjufvjafbxnbgriwgokdgqdqewn", "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq")
print(a)

