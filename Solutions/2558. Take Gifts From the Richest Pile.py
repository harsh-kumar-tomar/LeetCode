"""
Link: https://leetcode.com/problems/take-gifts-from-the-richest-pile
Difficulty: Easy
Space Complexity: O(n)
Time Complexity: O(n+k*logn)

Question:
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.



Example 1:

Input: gifts = [25,64,9,4,100], k = 4

Output: 29

Explanation:
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
Example 2:

Input: gifts = [1,1,1,1], k = 4

Output: 4

Explanation:
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
That is, you can't take any pile with you.
So, the total gifts remaining are 4.
"""

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        sum = 0

        for element in gifts:
            heapq.heappush(max_heap, -1 * element)

        while k != 0:
            k -= 1
            max_element = -1 * heapq.heappop(max_heap)
            max_element = int(math.sqrt(max_element))
            heapq.heappush(max_heap, -1 * max_element)

        for element in max_heap:
            sum += element

        return -1 * sum


# input : 5
# 4 run
# 3 run
# 2 run
# 1 run
# 0 run


Solution().pickGifts(gifts=[25, 64, 9, 4, 100], k=4)
