from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left+right)//2

            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                left = mid + 1
        
    

a = Solution().peakIndexInMountainArray(arr = [3,4,5,1])
print(a)