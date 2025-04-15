test = int(input())

for _ in range(test):
    s = list(input())
    s.reverse()

    n = len(s)

    for i in range(n):
        if s[i] == "q":
            s[i] = "p"
        elif s[i] == "p":
            s[i] = "q"

    print("".join(s))


    