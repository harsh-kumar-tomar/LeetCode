n = input()
n = n[1:len(n)-1].split(",")
s = set()
for i in n:
    if i.strip().isalpha():
        s.add(i.strip())

print(len(s))
print(s)