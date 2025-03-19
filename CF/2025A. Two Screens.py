
test = int(input())


for _ in range(test):
    word1 = input()
    n1 = len(word1)
    word2 = input()
    n2 = len(word2)
    same_characters = 0

    min_length = min(n1,n2)

    for i in range(min_length):
        if word1[i] == word2[i]:
            same_characters += 1
        else:
            break

    print(n1 + n2 - same_characters + (1 if same_characters !=0 else 0))


