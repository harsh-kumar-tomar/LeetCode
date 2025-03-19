from typing import  List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        timeInterval = []
        sum = 0

        for time in timeSeries:
            timeInterval.append([time, time + duration - 1])

        timeInterval.sort(key=lambda x: x[0])

        r = [timeInterval[0]]

        for interval in timeInterval:
            if r[-1][1] > interval[0]:
                r[-1][1] = max(r[-1][1], interval[1])
            else:
                r.append(interval)

        for time in r:
            sum += time[1] - time[0] + 1

        return sum

a = Solution().findPoisonedDuration( timeSeries = [1,2], duration = 2)