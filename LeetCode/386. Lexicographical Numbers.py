
from typing import List

def lexicalOrder(n: int) -> List[int]:
    ls = []
    for i in range(1,10):
        recursion(i,n,ls)
    
    return ls


def recursion(x,n,ls):
    if x > n:
        return
    
    ls.append(x)

    for i in range(0,10):
        num = x*10 + i
        recursion(num,n,ls)


a = lexicalOrder(16)
print(a)
