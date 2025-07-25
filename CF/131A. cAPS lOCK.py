s = input()
first_cap = s[0].isupper()
second_cap = True
ans = [s[0].upper()]

for i in range(1,len(s)):
    if s[i].islower():
        second_cap = False
    ans.append(s[i].lower())

if first_cap and second_cap:
    print(s.lower())
elif not first_cap and second_cap:
    print("".join(ans))
else:
    print(s)
