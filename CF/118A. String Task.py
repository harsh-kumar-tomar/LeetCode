s = input()
r = []
for char in s:
    if char not in "aeiouAEIOUyY":
        r.append(".")
        r.append(char.lower())

print("".join(r))
            