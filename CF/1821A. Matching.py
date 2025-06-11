test = int(input())

for _ in range(test):
    s = input()
    count = 1

    for i in range(len(s)):
        if i == 0 and s[i] == "?":
            count *= 9
        elif s[i] == "?":
            count *= 10
            
    print(0 if s[0] == "0" else count)