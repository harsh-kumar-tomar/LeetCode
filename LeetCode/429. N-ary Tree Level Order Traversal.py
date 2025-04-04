
from typing import *

from categories import Categories
import queue

path = Categories.TREE

def levelOrder(self, root: 'Node') -> List[List[int]]:
    r = []

    q = queue.Queue()
    q.put(root)

    while not q.empty():

        level_size = q.qsize()
        ls = []

        for _ in range (level_size):

            el = q.get()

            ls.append(el.val)

            for child in el.children:
                if child:
                    q.put(child)

        r.append(ls)

    return r




