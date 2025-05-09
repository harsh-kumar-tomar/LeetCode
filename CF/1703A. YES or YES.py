test = int(input())

for _ in range(test):
    s = input()

    if (s[0] == "y" or s[0] == "Y") and (s[1] == "e" or s[1] == "E") and (s[2] == "S" or s[2] == "s"):
        print("YES")
    else:
        print("NO") 
