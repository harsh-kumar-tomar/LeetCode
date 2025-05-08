s = input()
count_upper = 0
count_lower = 0

for char in s:
    if char.isupper():
        count_upper += 1
    else:
        count_lower += 1

if count_lower - count_upper >= 0:
    print(s.lower())
else:
    print(s.upper())