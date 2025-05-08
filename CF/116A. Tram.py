stops = int(input())
capacity = 0

count = 0
for _ in range(stops):
    exit,enter = map(int,input().split())
    count += (enter- exit)
    capacity = max(count,capacity)

print(capacity)


