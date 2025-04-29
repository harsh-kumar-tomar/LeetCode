
def recursion(i,index,ls):
    if index == len(arr):
        return False
    if i == 0:
        print(ls)
        return True
    if i < 0 :
        return False
    
    ls.append(arr[index])
    a = recursion(i-arr[index],index+1,ls) 
    ls.pop()
    b = recursion(i,index+1,ls)


n = int(input())
arr = [i for i in range(1,n+1)]
total_sum = n*(n+1)//2

if total_sum % 2 == 1:
    print("NO")
else:
    temp = recursion(total_sum//2,0,[])
