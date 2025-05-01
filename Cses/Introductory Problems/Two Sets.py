import sys
sys.setrecursionlimit(10**6)

def recursion(i,index,ls):
    if index == len(arr):
        return False
    if i == 0:
        global ans 
        ans = set(ls)
        return True
    if i < 0 :
        return False
    
    ls.append(arr[index])
    a = recursion(i-arr[index],index+1,ls) 
    ls.pop()
    b = recursion(i,index+1,ls)

    return a or b


n = int(input())
arr = [i for i in range(1,n+1)]
total_sum = n*(n+1)//2
ans = set()

if total_sum % 2 == 1:
    print("NO")
else:
    temp = recursion(total_sum//2,0,[])
    left_arr = list(ans)
    right_arr = []
    
    for i in range(1,n+1):
        if i not in ans:
            right_arr.append(i)
    print("YES")
    print(len(left_arr))
    print(*left_arr)
    
    print(len(right_arr))
    print(*right_arr)


"""
approach 1 

"""

n = int(input())
total_sum = sum(range(1,n+1))
half_sum = total_sum // 2

if half_sum % 2 == 1:
    print("NO")
else:
    arr1 = [] 
    arr2 = [] 
    
    for i in range(n,0,-1):
        if  half_sum >= i :
            half_sum -= i
            arr1.append(i)
        else:
            arr2.append(i)

    print("YES")
    print(len(arr1))
    print(*arr1)
    print(len(arr2))
    print(*arr2)
     
