test = int(input())

for _ in range(test):
    s = input()

    char1 = s[0]
    char2 = s[1]

    calc = 25*(ord(char1)-ord("a")) + (ord(char2)-ord("a") + 1 - (1 if ord(char2)>ord(char1)else 0))

    print(calc)