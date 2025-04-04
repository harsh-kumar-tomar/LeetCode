from LeetCode.TreeNode import TreeNode


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        s = [0]
        self.recursion(root, s)
        return s[0]

    def recursion(self, root, s):
        if not root:
            return (0, 0)

        left_sum, left_nodes = self.recursion(root.left, s)
        right_sum, right_nodes = self.recursion(root.right, s)

        total_sum = left_sum + right_sum + root.val
        total_nodes = left_nodes + right_nodes + 1

        if total_sum // total_nodes == root.val:
            s[0] += 1

        return total_sum, total_nodes
