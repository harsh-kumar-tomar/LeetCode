from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        left_score = [] # values[i]+i
        right_score = [] # values[j] - j
        max_score = float('-inf')

        n = len(values)

        for i in range(0,n):
            left_score.append(values[i]+i)

        for j in range(0,n):
            right_score.append(values[j]-j)

        max_left = left_score[0]
        for j in range(1,n):
            max_score = max(max_score,max_left+right_score[j])
            max_left = max(max_left,left_score[j])

        return max_score




        # Brute force , just finding out all the possible solution time complexity = O(n2)

        # n = len(values)
        # max = -1
        #
        # for i in range(n):
        #     for j in range(i+1,n):
        #         value = values[i] + values[j] + i - j
        #         if max < value:
        #             max = value
        #
        #
        # return max


a = Solution().maxScoreSightseeingPair(values = [8,1,5,2,6])
print(a)
# 1 1 1 1 1
# 0 1 2 3 4 5
