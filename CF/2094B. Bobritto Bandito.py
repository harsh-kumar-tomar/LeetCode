
test = int(input())

for _ in range(test):
    n , m ,l , r = list(map(int,input().split()))
    diff = n-m

    new_l = min(0,diff+l)
    diff = max(0,diff+l)

    new_r = max(0,r-diff)
    
    print(new_l,new_r)