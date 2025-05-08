n = int(input())
s = input()
count_a = 0
for char in s:
    if char == "A":
        count_a += 1

if count_a > n/2:
    print("Anton")
elif count_a == n /2:
    print("Friendship")
else:
    print("Danik")
