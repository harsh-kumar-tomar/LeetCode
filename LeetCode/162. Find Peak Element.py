"""
Link: https://leetcode.com/problems/first-bad-version/
Difficulty: Medium
Space Complexity: O(1)
Time Complexity: O(log(n))

Advice
See, binary search has two important aspects.

A sorted array.
Splitting an array into two halves.

Question

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""


def findPeakElement(self, nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    n = len(nums)

    while start <= end:
        mid = start + (end - start) // 2

        value_right = nums[mid + 1] if mid < n - 1 else float('-inf')
        value_left = nums[mid - 1] if mid > 0 else float('-inf')

        if value_left < nums[mid] > value_right:
            return mid
        elif nums[mid] > value_left:
            start = mid + 1
        else:
            end = mid - 1

    return start
