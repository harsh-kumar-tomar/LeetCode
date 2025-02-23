from typing import List


def match(text: str, pattern: str):
    index = []

    for i in range(len(text)-len(pattern)+1):
        if text[i] == pattern[0]:
            j = 0
            while j < len(pattern) and text[j + i] == pattern[j]:
                j += 1

            if j == len(pattern):
                index.append(i)

    return index


a = match("mississippi", "issipi")
print(a)
