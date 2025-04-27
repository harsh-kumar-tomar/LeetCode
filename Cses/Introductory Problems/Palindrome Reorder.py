s = input().strip()
hash_map = {}
count_odd = 0
char_odd = ""
r = []

for char in s:
    hash_map[char] = hash_map.get(char,0)+1

for val in hash_map.values():
    if val % 2 == 1:
        count_odd += 1

if count_odd > 1:
    print("NO SOLUTION")
else:
    for key,val in hash_map.items():
        if val % 2 == 0:
            temp = [key]*(val//2)
            hash_map[key] = hash_map.get(key)//2
            r = r + temp
        else:
            char_odd = key
    
    temp1 = [char_odd]*count_odd
    temp2 = r.copy()
    temp2.reverse()

    r = r + temp1 + temp2
    print("".join(r))
