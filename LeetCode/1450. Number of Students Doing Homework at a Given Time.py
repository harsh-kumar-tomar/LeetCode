from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        n = len(startTime)
        count = 0

        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        
        return count