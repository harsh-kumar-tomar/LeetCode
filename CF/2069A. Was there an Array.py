test = int(input())

for _ in range(test):
    n = int(input())
    char_arr = list(map(int,input().split()))
    
    arr = [-1]*n
    flag = True
    random_num = 1

    for i in range(0,n-2):

        if char_arr[i] == 1:
            if arr[i+1] == -1 and arr[i] == -1 and arr[i+2] == -1:
                arr[i] = arr[i+1] = arr[i+2] = random_num
            else:
                if char_arr[i-1] == char_arr[i]:
                    arr[i+2] = arr[i+1]
                else:
                    flag = False
        
        random_num += 1

    print("Yes") if flag else print("No")