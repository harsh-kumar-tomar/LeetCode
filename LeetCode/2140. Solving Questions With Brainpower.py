from typing import List


def mostPoints(self, questions: List[List[int]]) -> int:
    dp = [-1] * len(questions)
    return self.recursion(0, questions, 0, dp)


def recursion(self, curr_index, questions, points, dp):
    if curr_index >= len(questions):
        return 0

    if dp[curr_index] != -1:
        return dp[curr_index]

    # choose the current question
    q = questions[curr_index]
    a = q[0] + self.recursion(curr_index + q[1] + 1, questions, points + q[0], dp)

    # leave curr question
    b = self.recursion(curr_index + 1, questions, points, dp)
    dp[curr_index] = max(a, b)
    return dp[curr_index]


a = mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]])
print(a)


"""
using brute force 

def mostPoints(questions: List[List[int]]) -> int:
    dp = [0] * (len(questions) + 1)
    return recursion(0, questions, 0, dp)


def recursion(curr_index, questions, points, dp):
    if curr_index >= len(questions):
        return points

    # choose the current question
    q = questions[curr_index]
    a = recursion(curr_index + q[1] + 1, questions, points + q[0], dp)

    # leave curr question
    b = recursion(curr_index + 1, questions, points, dp)

    return max(a, b)

"""