from typing import *

from Solutions.Tree.TreeNode import TreeNode
from categories import Categories
import queue

path = Categories.TREE


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    r = []
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        level_size = q.qsize()
        s = 0
        count = level_size

        for _ in range(level_size):
            el = q.get()
            s += el
            if el.left:
                q.put(el.left)
            if el.right:
                q.put(el.right)

        r.append(s/count)

    return r


