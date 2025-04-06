import heapq
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    heap = []
    index = 0

    for i in range(1, len(heights)):
        diff = heights[i] - heights[i - 1]
        pop_el = float('inf')

        if diff > 0:
            if ladders > 0:
                ladders -= 1
            else:
                if heap:
                    pop_el = heapq.heappop(heap)
                min_jump = min(pop_el, diff)

                if bricks >= min_jump:
                    bricks -= min_jump
                else:
                    break

            heapq.heappush(heap, max(pop_el, diff) if pop_el != float('inf') else diff)

        index += 1

    return index


a = furthestBuilding(heights=[14, 3, 19, 3], bricks=17, ladders=0)
print(a)
