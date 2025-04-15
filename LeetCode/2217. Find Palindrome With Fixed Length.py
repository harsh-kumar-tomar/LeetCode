
from typing import List


def kthPalindrome(queries: List[int], intLength: int) -> List[int]:
    half_digit = (intLength+1)//2
    min_number = 10**(half_digit-1)
    max_combination = 9*min_number
    
    result = []

    for query in queries:
        temp = str(min_number + query -1)

        if query <= max_combination:
            if intLength % 2 == 0:
                result.append(temp+temp[::-1])
            else:
                result.append(temp+temp[1::-1])
        else:
            result.append(-1)
    
    return result


a = kthPalindrome(queries = [2,4,6], intLength = 4)
# print(a)
char = "12345"
print(char[1::-1])
print(char[:-1][::-1])
"""

Question
How to find out the exact min number of k digit , and that will palindrome ?
hint : think do we really have to consider all digit places , as it is palindrome , we should only consider n//2 places only .

"""