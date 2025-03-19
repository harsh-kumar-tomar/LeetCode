n = input()
count = 0

for i in n:
    if i == "4" or i == "7":
        count += 1


print("Yes") if count == 7 or count == 4 else print("No")