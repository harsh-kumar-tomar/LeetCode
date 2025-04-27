n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    arr[i] -= 1

flag = False
for i in range(n):
    if arr[arr[arr[i]]] == i:
        flag = True
        break

print("Yes") if flag == True else print("No")


