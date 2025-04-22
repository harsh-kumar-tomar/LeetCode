test = int(input())

def visit(index,val):
    
    if val in s:
        if val == arr[index]:
            return False
        else:
            return True
    else:
        s.add(index)
        return visit(val,arr[val])



for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    s = set()

    for i in range(n):
        arr[i] -= 1

    flag = False
    for index,val in enumerate(arr):
        if index not in s:
            if visit(index,val):
                flag = True
                break
    
    print("Yes") if flag == True else print("No")


