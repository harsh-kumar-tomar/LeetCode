
import sys


input = sys.stdin.read
data = input().split()

idx = 0
test = int(data[idx])
idx += 1

for _ in range(test):
    n = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx+n]))
    idx += n

    s = set()
    r = []
    generate_num = 1
    all_numbers = set(range(1,n+1))
    number_seen = set(arr)
    number_not_seen = list(all_numbers-number_seen)

    for i in range(n):

        if arr[i] in s:
            r.append(number_not_seen.pop())
        else:
            s.add(arr[i])   
            r.append(arr[i])

    print(*r)
    