n = int(input())
a,*p = map(int,input().split())
b,*q = map(int,input().split())

s = set()

for i in p:
    s.add(i)
for i in q:
    s.add(i)

if len(s) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
