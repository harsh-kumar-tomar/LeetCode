n = int(input())

def is_unique(num):
    s = set()
    while num != 0:
        rem = num % 10
        num = num // 10
        if rem not in s:
            s.add(rem)
        else:
            return False
    
    return True

while True:
    n += 1
    if is_unique(n):
        break

print(n)


