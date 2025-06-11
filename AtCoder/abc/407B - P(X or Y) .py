add , sub = map(int,input().split())
total_combination = 36

one_condition = set()

for i in range (1,7):
    for j in range (1,7):
        if i+j >= add:
            one_condition.add((i,j))
        if abs(i-j) >= sub:
            one_condition.add((i,j))

print(len(one_condition)/total_combination)