test = int(input())

for _ in range(test):
    n , k = map(int,input().split())
    arr = input()

    hash_map = {}

    for i in arr:
        hash_map[i] = hash_map.get(i,0) + 1
    
    odd_num = 0
    even_num = 0
    for key,value in hash_map.items():
        if value%2 == 1:
            odd_num += 1 

    k = k-odd_num

    print("YES") if k >= 0 and k%2 == 0 else print("NO")