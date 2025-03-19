
test = int(input())

for _ in range(test):
    a,b = map(int,input().split())

    print("Yes") if (a-b+1)/9 == (a-b+1)//9 and (a-b+1)>=0 else print("No")