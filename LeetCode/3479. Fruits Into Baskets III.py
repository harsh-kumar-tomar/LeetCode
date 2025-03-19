
from typing import *

def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    fruits.sort()
    baskets.sort()

    j = 0
    count = 0

    for fruit in fruits:

        while j < len(baskets) and baskets[j] < fruit:
            j += 1

        if j < len(baskets):
            j += 1
        else:
            count += 1

    return count


a = numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4])
print(a)

