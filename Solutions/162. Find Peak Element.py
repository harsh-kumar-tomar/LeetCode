def findPeakElement(self, nums: List[int]) -> int:
    start = 0
    end = len(nums) - 1
    n = len(nums)

    while start <= end:
        mid = start + (end - start) // 2

        value_right = nums[mid + 1] if mid < n - 1 else float('-inf')
        value_left = nums[mid - 1] if mid > 0 else float('-inf')

        if value_left < nums[mid] > value_right:
            return mid
        elif nums[mid] > value_left:
            start = mid + 1
        else:
            end = mid - 1

    return start
