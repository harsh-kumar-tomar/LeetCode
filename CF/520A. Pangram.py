n = int(input())
s = input()
a = set()
for char in s:
    a.add(char.lower())

if len(a) == 26:
    print("YES")
else:
    print("NO")