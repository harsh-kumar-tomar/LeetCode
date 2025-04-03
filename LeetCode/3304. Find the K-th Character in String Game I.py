

def kthCharacter(k: int) -> str:
    word = ["a"]

    while len(word) < k:
        temp = []
        for char in word:
            next_char = chr(ord('a') + (ord(char) - ord('a') + 1) % 26)
            temp.append(next_char)

            if len(word)+len(temp) == k:
                break
        word = word+temp

    return word[k-1]



a = kthCharacter(10)
print(a)

