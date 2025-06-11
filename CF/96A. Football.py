s = input()
count_zero = 0
count_one = 0
dangerous = False

for el in s:
    if el == "0":
        count_zero += 1
        count_one = 0
    else:
        count_one += 1
        count_zero = 0
    
    if count_zero >= 7 or count_one >= 7:
        dangerous = True
        break
    
print("YES") if dangerous else print("NO")