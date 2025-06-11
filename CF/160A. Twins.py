n = int(input())

arr = list(map(int,input().split()))

coin = 0
pair1 = 0
pair2 = sum(arr)
arr.sort(reverse=True)

for el in arr:
    pair1 += el
    coin += 1
    pair2 -= el
    if pair1 > pair2:
        break

print(coin)