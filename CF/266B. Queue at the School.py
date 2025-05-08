n , t = map(int,input().split())
arr = list(input())

while t !=0 :
    i = 0
    while i < n -1:
        if arr[i] == "B" and arr[i+1] == "G":
            arr[i] , arr[i+1] = arr[i+1] , arr[i]
            i += 2
        else:
            i += 1
    t -= 1
print("".join(arr)) 