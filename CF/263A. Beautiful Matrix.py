ls = []
for i  in range(0,5):
    temp = list(map(int,input().split()))
    ls.append(temp)
x = 0
y = 0

for i in range(0,5):
    for j in range(0,5):
        if ls[i][j] == 1:
            x,y = i, j
            break

print(abs(2-y)+abs(2-x))