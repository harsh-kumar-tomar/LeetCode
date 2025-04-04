from typing import Optional

from LeetCode.TreeNode import TreeNode


def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    self.recursion(root1, root2)
    return root1 if root1 else root2


def recursion(self,root1,root2):

    if not root1 or not root2:
        return

    if not root1.left and root2.left:
        root1.left, root2.left = root2.left, root1.left

    if not root1.right and root2.right:
        root1.right, root2.right = root2.right, root1.right

    root1.val += root2.val

    self.recursion(root1.left,root2.left)
    self.recursion(root1.right,root2.right)

