# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Solutions.Tree.TreeNode import TreeNode


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        self.preorder(root, arr)

        prev_node = None
        main_root = None

        # print(arr)

        for value in arr:
            current_node = TreeNode(value, None, None)

            if prev_node:
                prev_node.right = current_node
            else:
                main_root = current_node

            prev_node = current_node

        return main_root

    def preorder(self, root, arr):

        if not root:
            return

        if not root.left and not root.right:
            arr.append(root.val)
            return

        self.preorder(root.left, arr)
        arr.append(root.val)
        self.preorder(root.right, arr)

