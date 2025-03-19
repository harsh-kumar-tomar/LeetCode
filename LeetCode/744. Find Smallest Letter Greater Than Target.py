"""
Link: https://leetcode.com/problems/first-bad-version
Difficulty: Easy
Space Complexity: O(1)
Time Complexity: O(log(n))

Question:
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        start = 0
        end = len(letters) - 1
        n = len(letters)
        target = ord(target)

        while start <= end:
            mid = start + (end - start) // 2

            if ord(letters[mid]) == target:
                start = mid + 1
                # return letters[mid+1] if mid < n-1 else letters[0]
            elif ord(letters[mid]) > target:
                end = mid - 1
            else:
                start = mid + 1

        return letters[start] if start < n else letters[0]
