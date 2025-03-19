from typing import List


def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)

    def check(k):
        diff_array = [0] * (n + 1)

        for i in range(k + 1):
            l, r, val = queries[i]
            diff_array[l] -= val
            diff_array[r + 1] += val

        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += diff_array[i]

            if nums[i] + prefix_sum > 0:
                return False

        return True

    left, right = 0, len(queries) - 1
    index = -1

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            index = mid
            right = mid - 1
        else:
            left = mid + 1

    return index+1 if index != -1 else index


a = minZeroArray(nums=[5], queries=[[0,0,5],[0,0,1],[0,0,3],[0,0,2]])
print(a)

# approach 1

# def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
#     query_count = 0
#     arr_sum = sum(nums)
#
#     if arr_sum == 0 :
#         return 0
#
#     for query in queries:
#         l, r, val = query
#         for i in range(l, r + 1):
#             if nums[i] != 0:
#                 arr_sum -= min(nums[i],val)
#                 nums[i] = max(0, nums[i] - val)
#
#         query_count += 1
#
#         if arr_sum == 0:
#             return query_count
#
#     return -1
