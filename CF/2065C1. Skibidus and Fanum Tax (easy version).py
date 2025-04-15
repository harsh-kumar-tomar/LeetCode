
test = int(input())

for _ in range(test):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    good = True

    # setting max val for last item

    for i in range(n-1,-1,-1):

        if i == n-1:
            a[n-1] = max(a[n-1],b[0]-a[n-1])
            continue

        if a[i] > a[i+1]:
            a[i] = b[0] - a[i]
        else:
            if b[0] - a[i] <= a[i+1]:
                a[i] = max(a[i],b[0]-a[i])
        
        if a[i] > a[i+1]:
            good = False
            break
    
    print("Yes") if good else print("No")


"""
mistake : always check sign like < or <= 
"""