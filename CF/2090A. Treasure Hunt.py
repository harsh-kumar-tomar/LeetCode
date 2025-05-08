test = int(input())

for _ in range(test):
    x,y,a = map(int,input().split())
    a = 5*a

    if a%(x+y) == 0:
        print("YES")
    else:
        a = a % (x+y)

        if x >= a  :
            print("NO")
        else:
            print("YES")