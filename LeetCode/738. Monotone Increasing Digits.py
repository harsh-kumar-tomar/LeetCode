import math

def monotoneIncreasingDigits(n: int) -> int:
    right = n
    left = 0

    while left < right:
        mid = math.ceil((right + left)/2)

        if is_good(mid):
            left = mid
        else:
            right = mid - 1

    return left 
    

def is_good(n)->bool:
    string = str(n)

    temp = string[0]

    for index in range(1,len(string)):
        if temp <= string[index]:
            temp = string[index]
        else:
            return False
    
    return True



a = monotoneIncreasingDigits(1234)
print(a)