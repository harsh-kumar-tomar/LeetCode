from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        halfSum = s / 2
        operation = 0
        currentSum = s
        max_heap = MaxHeap()

        for i in nums:
            max_heap.push(i)

        while currentSum > halfSum:
            bigNum = max_heap.pop()
            bigNum = bigNum / 2
            currentSum -= bigNum

            max_heap.push(bigNum)
            operation += 1

        return operation


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)