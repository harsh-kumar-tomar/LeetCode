def visit(i):
    if i in index:
        if arr[arr[i]] == i:
            return False
        else:
            return True
    index.add(i)
    return visit(arr[i])



n = int(input())
arr = list(map(int,input().split()))
index = set()

for i in range(n):
    arr[i] -= 1

flag = False
for i in range(n):
    if index not in index:
        index.add(i)
        if visit(arr[i]):
            flag = True
            break

print("Yes") if flag == True else print("No")


