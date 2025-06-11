n = int(input())

for _ in range(n):
    n , k = map(int,input().split())
    s = input()
    z = s.count('0')
    o = s.count('1')
    
    max_pairs = n // 2
    bad_pairs = max_pairs - k
    
    if 0 <= k <= max_pairs and z >= bad_pairs and o >= bad_pairs:
        print("YES")
    else:
        print("NO") 