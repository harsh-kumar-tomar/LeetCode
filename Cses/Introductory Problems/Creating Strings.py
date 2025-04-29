
def recursion(temp:list[int]):
    if len(arr) == len(temp):
        r.append("".join(temp))
        return

    for i in range(n):
        
        if i >0 and arr[i] == arr[i-1] and not used[i-1]:
            continue

        if not used[i] :
            used[i] = True
            temp.append(arr[i])
            recursion(temp)
            temp.pop()
            used[i] = False

arr = list(input())
arr.sort()
r = []
n = len(arr)
used = [False]*len(arr)
recursion([])
print(len(r))
for i in r:
    print(i)