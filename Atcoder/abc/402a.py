n = input()
s = []
for i in n:
    if i.isupper():
        s.append(i)

print("".join(s))
