
test = int(input())

for _ in range(test):
    x = int(input())
    founded = False
    for y in range(x-1,0,-1):
        xor = x^y
        if x < xor + y and y < x + xor and xor < x+y:
            print(y)
            founded = True
            break

    if not founded:
        print(-1)
