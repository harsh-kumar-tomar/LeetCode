n = int(input())
count = 1
prev= input()
for _ in range(n-1):
    curr = input()

    if prev != curr:
        count += 1
    prev = curr

print(count)