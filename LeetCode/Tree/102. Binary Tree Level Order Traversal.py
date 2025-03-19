from typing import *

from LeetCode.Tree.TreeNode import TreeNode
from categories import Categories
import queue

path = Categories.TREE


def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    q = queue.Queue()
    r = []

    q.put(root)

    while not q.empty():
        level_size = q.qsize()
        ls = []
        for _ in range(level_size):
            el = q.get()
            ls.append(el.val)
            if el.left:
                q.put(el.left)
            if el.right:
                q.put(el.right)

        r.append(ls)

    return r
