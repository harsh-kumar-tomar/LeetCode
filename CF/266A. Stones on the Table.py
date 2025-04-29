n = int(input())
s = input()
r = [s[0]]

for i in range(1,n):
    el = s[i]
    if el != r[-1]:
        r.append(el)

print(len(s)-len(r))