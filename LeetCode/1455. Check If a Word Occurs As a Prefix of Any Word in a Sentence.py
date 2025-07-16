class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        n = len(searchWord)

        for index , word in enumerate(sentence):
            j = 0
            for char in word:
                if  j >= n or char != searchWord[j] :
                    break
                j += 1

            if j == len(searchWord):
                return index + 1

        return -1     
