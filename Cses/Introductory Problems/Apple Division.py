n = int(input())
arr = list(map(int,input().split()))

def recursion(i,sum1,sum2):
    if i == n:
        return abs(sum1-sum2)
    
    return min(recursion(i+1,sum1+arr[i],sum2) , recursion(i+1,sum1,sum2+arr[i]) )


a = recursion(0,0,0)
print(a)
