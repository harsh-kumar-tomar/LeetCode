
from typing import *
from queue import *

def numberOfAlternatingGroups(colors: List[int], k: int) -> int:


    if len(colors) < k :
        return 0

    q = Queue()
    n = len(colors)

    for i in range(n):
        q.put(colors[i])

    for i in range(k-1):
        q.put(colors[i])


    temp_element = q.get()
    window = 1
    count_window = 0
    while not q.empty():
        current_element = q.get()

        if temp_element != current_element:
            temp_element = current_element
            window += 1
        else:
            window = 1

        if window >= k:
            count_window += 1

    return count_window


a = numberOfAlternatingGroups(colors = [1,1,0,1], k = 4)
print(a)