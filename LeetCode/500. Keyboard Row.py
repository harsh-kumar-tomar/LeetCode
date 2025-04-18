"""
Link: https://leetcode.com/problems/keyboard-row
Difficulty: Medium
Space Complexity: O(n)
Time Complexity: O(n*k)

Question

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".



Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]

Output: ["Alaska","Dad"]

Explanation:

Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:

Input: words = ["omk"]

Output: []

Example 3:

Input: words = ["adsdf","sfd"]

Output: ["adsdf","sfd"]



Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""

import heapq
import math
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        ls = []

        for word in words:
            n = len(word)
            firstRow = 0
            secondRow = 0
            thirdRow = 0

            for char in word:
                char = str.lower(char)
                if char in "qwertyuiop":
                    firstRow += 1
                if char in "asdfghjkl":
                    secondRow += 1
                if char in "zxcvbnm":
                    thirdRow += 1

            if firstRow == n or secondRow == n or thirdRow == n:
                ls.append(word)

        print(ls)

# can use set as it will avoid the 'in' operation which can take m time complexity




Solution().findWords(words = ["Hello","Alaska","Dad","Peace"])
