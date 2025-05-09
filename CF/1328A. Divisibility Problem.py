test = int(input())

for _ in range(test):
    a ,b = map(int,input().split())
    print((b*((a+b-1)//b))-a)