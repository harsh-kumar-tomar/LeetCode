
def recursion(s:list[int],l:int):
    if l == 0:
        print("".join(s))
        return

    s.append("0")
    recursion(s,l-1)
    s.pop()
    s.append("1")
    recursion(s,l-1)
    s.pop()


n = int(input())
recursion([],n)