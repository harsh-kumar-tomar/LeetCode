test = int(input())

for _ in range(test):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))

    i = 0
    is_activated = False
    while i < n and x >= 0:
        if arr[i] == 1:
            is_activated = True
        
        if is_activated:
            x -= 1
        
        if x == 0:
            is_activated = False
        
        i += 1

    if i == n:
        print("YES")
    else:
        print("NO")
