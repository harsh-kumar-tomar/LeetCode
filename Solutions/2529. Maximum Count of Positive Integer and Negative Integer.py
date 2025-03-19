from typing import List


def maximumCount(nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] > 0:
            end = mid
        else:
            start = mid + 1

    positive_index = mid if nums[mid] > 0 else -1

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1

    negative_index = mid if nums[mid] < 0 else - 1

    positive_count = (len(nums) - positive_index) if positive_index != -1 else 0
    negative_count = (negative_index + 1) if negative_index != -1 else 0

    return max(negative_count, positive_count)


a = maximumCount([-1563,-236,-114,-55,427,447,687,752,1021,1636])
print(a)