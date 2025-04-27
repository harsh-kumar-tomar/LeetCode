test = int(input())

for _ in range(test):
    n , k = map(int,input().split())

    odd_calc = n - k + 1
    even_calc = n - 2*k + 2
    arr = []

    if odd_calc >= 0 and odd_calc %2 == 1:
        arr =[1]*(k-1)+[odd_calc]
    elif even_calc >= 0 and even_calc % 2 == 0:
        arr = [2]*(k-1)+[even_calc]
    else:
        print("No")
        continue
    
    print("Yes")
    print(*arr)
