from collections import deque
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    prefix_sum = [0]
    suffix_sum = deque([0])

    for i in range(n-1):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for i in range(n - 1, 0, -1):
        suffix_sum.appendleft(suffix_sum[0] + nums[i])

    for i in range(1,n-1):
        if prefix_sum[i] == k or suffix_sum[k] == k or prefix_sum[i]+nums[i] == k or suffix_sum[i]+nums[i] == k or nums[k] == k:
            count += 1

    print(prefix_sum, suffix_sum)


a = subarraySum(nums=[1, 2, 3], k=3)
print(a)
