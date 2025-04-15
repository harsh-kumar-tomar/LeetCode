
test = int(input())

for _ in range(test):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    good = True

    for i in range(n-2,-1,-1):
        if a[i] > a[i+1]:
            a[i] = b[0] - a[i]
        
        if a[i] > a[i+1]:
            good = False
            break
    
    print("Yes") if good else print("No")