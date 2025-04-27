test = int(input())

for _ in range(test):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    add = 0
    solution_exists = True
    position_available  = 0
    min_a = min(a)
    max_a = max(a)
    
    for i in range(n):
        if b[i] != -1:
            if add == 0:
                add = a[i] + b[i]
            else:
                print(0)
                solution_exists = False
        
        if b[i] == -1:
            position_available += 1

    if solution_exists:
        if position_available == n:
            minimum = min(a)
            maximum = max(a)
            sol = k - (maximum - minimum) + 1
            if sol >= 0 :
                print(sol)
            else:
                print(0) 

        else:
            print(1)
    print("*************")
