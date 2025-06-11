s = input()

flag = False

for char in s:
    if char == "H" or char == "Q"  or char == "9":
        flag = True


print("YES") if flag else print("NO")