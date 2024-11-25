# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start = 0
        end = n

        while start <= end:
            mid = start + (end-start)//2
            bad_version = isBadVersion(mid)

            if not bad_version:
                start = mid + 1
            else:
                end = mid - 1
        
        return start

            
        