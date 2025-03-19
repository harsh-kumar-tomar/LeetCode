
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        count = 0
        for fruit in fruits:
            placed = False
            for index, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[index] = -1
                    placed = True
                    break

            if not placed:
                count += 1

        return count
