# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)

    def reverse(self,root):

        if root == None or root.next == None:
            return root

        ls = self.reverse(root.next)
        root.next.next = root
        root.next = None

        return ls