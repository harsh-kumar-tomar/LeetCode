n,k = map(int,input().split())
x,a,b,c = map(int,input().split())

arr = [x]
minimum = x

for i in range(k):
    el = (a*arr[-1]+b)%c
    minimum = min(minimum,el)
    arr.append(el)

for i in range(k,len(arr)):
    

