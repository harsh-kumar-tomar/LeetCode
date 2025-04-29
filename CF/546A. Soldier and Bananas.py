icost , idollar , total_banana = map(int,input().split())

total_banana_cost = icost*(total_banana)*(total_banana+1)//2

print(max(0,total_banana_cost - idollar))

