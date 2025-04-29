
def recursion(i)->list[int]:
    if i == 1:
        return [["0"],["1"]]
    
    ls = recursion(i-1)
    r = []

    for arr in ls:
        temp = arr.copy()
        temp.append("0")
        r.append(temp)

    ls.reverse()

    for arr in ls:
        temp = arr.copy()
        temp.append("1")
        r.append(temp)
    
    return r

n = int(input())
temp = recursion(n)

for i in temp:
    print("".join(i))


