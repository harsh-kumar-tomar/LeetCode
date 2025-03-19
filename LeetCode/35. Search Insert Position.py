def binary():
    nums = [1,2,4,6,7]
    target = 0
    n = len(nums)
    start = 0
    end = n - 1
    mid = 0

    while start <=  end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


    return mid if target < nums[mid] else mid + 1


a = binary()
print(a)
