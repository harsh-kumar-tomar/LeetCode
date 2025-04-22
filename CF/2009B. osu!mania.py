test = int(input())

for _ in range(test):
    n = int(input())
    arr = []

    for _ in range(n):
        temp = list(input())
        arr.append(temp)

    beat_arr = []
    for row in arr:
        for i in range(4):
            if row[i] == "#":
                beat_arr.append(i+1)
            
    beat_arr.reverse()    
    print(*beat_arr)