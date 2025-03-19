def countOfSubstrings(word: str, k: int) -> int:

    vowel = {}
    n = len(word)
    count_consonants = 0
    count_substring = 0

    start = 0

    for index, char in enumerate(word):

        if char in "aeiou":
            vowel[char] = vowel.setdefault(char, 0) + 1
        else:
            count_consonants += 1

        if count_consonants > k or index == n - 1:
            while count_consonants > k:
                temp_char = word[start]
                if word[start] in "aeiou":
                    vowel[temp_char] = vowel.get(temp_char) - 1
                    if vowel[temp_char] == 0:
                        vowel.pop(temp_char)
                    if len(vowel) == 5:
                        count_substring += 1
                else:
                    count_consonants -= 1

                start += 1

        if count_consonants == k and len(vowel) == 5:
            count_substring += 1

            if index < n-1 and word[index] not in "aeiou" :
                temp_vowel = vowel.copy()
                temp_consonants = count_consonants
                temp_start = start
                while temp_consonants == k:
                    temp_char = word[temp_start]
                    if word[temp_start] in "aeiou":
                        temp_vowel[temp_char] = temp_vowel.get(temp_char) - 1
                        if temp_vowel[temp_char] == 0:
                            break
                        if len(temp_vowel) == 5:
                            count_substring += 1
                    else:
                        temp_consonants -= 1

                    temp_start += 1

    return count_substring


a = countOfSubstrings( word = "ieaouqqieaouqq", k = 1)
print(a)
