test = int(input())

for _  in range(test):
    a , b = map(int,input().split())
    yes = False
    
    if a == b:
        if a % 3 == 0 :
            yes = True
    elif a > b:
        if a / 2 == b:
            yes = True
    else:
        if b / 2 == a:
            yes = True
    
    print("YES") if yes else print("NO")