
import heapq

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)

    while len(arr) != 1:
        a1 = heapq.heappop(arr)
        a2 = heapq.heappop(arr)
        heapq.heappush(arr,a1+a2-1)

    print(arr[0])