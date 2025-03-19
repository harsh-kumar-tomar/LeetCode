from typing import List


def totalFruit(fruits: List[int]) -> int:
    start = 0
    hs = {}
    max_fruits = 0

    for index, fruit in enumerate(fruits):

        if fruit in hs or len(hs) < 2:
            hs[fruit] = hs.setdefault(fruit, 0) + 1
        else:
            while len(hs) == 2:
                temp_index = fruits[start]
                hs[temp_index] = hs.get(temp_index) - 1
                if hs.get(temp_index) == 0:
                    hs.pop(temp_index)
                start += 1

            hs[fruit] = 1

        max_fruits = max(max_fruits, index - start + 1)

    return max_fruits


a = totalFruit(fruits=[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
print(a)
