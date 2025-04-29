s = input()
count = 1
n = len(s)
dangerous = False

for i in range(1,n):

    if s[i] == s[i-1]:
        count += 1
    else:
        count = 1

    if count == 7:
        dangerous = True
        break

print("YES") if dangerous else print("NO")