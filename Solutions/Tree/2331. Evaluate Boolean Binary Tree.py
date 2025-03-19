from typing import Optional

from Solutions.Tree.TreeNode import TreeNode


def evaluateTree(self, root: Optional[TreeNode]) -> bool:

    if root.val == True or root.val == False:
        return root.val


    if root == 2:
        return self.evaluateTree(root.left) or self.evaluateTree(root.right)
    else:
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)

