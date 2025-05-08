import math
from functools import reduce


def gcd_list(arr):
    return reduce(math.gcd, arr)

test = int(input())

for _ in range(test):

    n = int(input())
    arr = list(map(int,input().split()))
    s = set(arr)

    if len(s) == 1:
        print("No")
        continue
    
    for i in range(n):
        B = [arr[i]]
        C = arr[:i]+arr[i+1:]

        if gcd_list(B) != gcd_list(C) :
            print("Yes")
            for j in range(n):
                if j != i:
                    print(2,end=" ")
                else:
                    print(1,end=" ")
            break


        