
x = int(input())
ls = []

for i in range(5,0,-1):
    ls.append(x//i)
    x = x % i

print(sum(ls))