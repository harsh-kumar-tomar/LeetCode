"""
Link: https://leetcode.com/problems/reverse-linked-list
Difficulty: Easy
Space Complexity: O(n)
Time Complexity: O(n)

Question:

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)

    def reverse(self, root):
        if root is None or root.next is None:
            return root

        ls = self.reverse(root.next)
        root.next.next = root
        root.next = None

        return ls


# Another appraoch

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ls = [None]
        self.recursion(head, ls)
        head.next = None
        return ls[0]

    def recursion(self, curr_node, ls):
        if curr_node.next == None:
            ls[0] = curr_node
            return curr_node

        next_node = self.recursion(curr_node.next, ls)
        next_node.next = curr_node

        return curr_node