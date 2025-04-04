"""
Link: https://leetcode.com/problems/count-vowel-strings-in-ranges
Difficulty: Medium
Space Complexity: O(n)
Time Complexity: O(n)

Question

2559. Count Vowel Strings in Ranges
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].


Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length
"""

from typing import List


class Solution:

    # version 1
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ls = []
        presum = []
        result = []

        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                ls.append(1)
            else:
                ls.append(0)

        temp = 0

        for value in ls:
            temp += value
            presum.append(temp)

        for query in queries:
            l, r = query
            result.append(presum[r] - (0 if l == 0 else presum[l-1] ))


        return result

  # version 2 directly filling presum list rather than first allocating 0,1 than tranversing again for presum
    def vowelStrings2(self, words: List[str], queries: List[List[int]]) -> List[int]:

        presum = []
        result = []
        s = {"a","e","i","o","u"}
        sum = 0

        for word in words:
            if word[0] in s and word[-1] in s:
                sum += 1
            presum.append(sum)

        for query in queries:
            l, r = query
            result.append(presum[r] - (0 if l == 0 else presum[l-1] ))


        return result


a = Solution().vowelStrings2( words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])
print(a)
