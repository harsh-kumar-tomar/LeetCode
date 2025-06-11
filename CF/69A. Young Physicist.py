n = int(input())
x = 0
y = 0
z = 0
for _ in range(n):
    tempx , tempy , tempz = map(int,input().split())

    x +=tempx
    y +=tempy
    z +=tempz

print("YES") if x == 0 and y==0 and z == 0 else print("NO")