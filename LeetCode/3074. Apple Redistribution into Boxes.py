from typing import List


def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    apples = sum(apple)
    num_of_boxes = 0

    
    capacity.sort()
    capacity.reverse()

    i = 0

    while apples > 0 and i < len(capacity):
        apples -= capacity[i]
        num_of_boxes += 1

        i+= 1

    return num_of_boxes

a = minimumBoxes(apple = [5,5,5], capacity = [2,4,2,7])
print(a)
