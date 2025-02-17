from typing import List

def countPartitions(nums: List[int]) -> int:
    prefixSum = []
    suffixSum = []
    totalSum = 0
    count = 0

    for i in nums:
        totalSum += i
        prefixSum.append(totalSum)

    for i in nums:
        suffixSum.append(totalSum)
        totalSum -= i

    for index in range(len(nums)-1):
        tempPrefix = prefixSum[index]
        tempSuffix = suffixSum[index] - nums[index]

        if abs(tempPrefix - tempSuffix) % 2 == 0:
            count += 1


    return count


a = countPartitions( nums =  [2,4,6,8])
print(a)




