test = int(input())

for _ in range(test):
    n = int(input())
    zero = 1
    # to store each round number
    r = [] 

    while n != 0:
        ten = 10**zero

        if n%ten !=0 :
            r.append(n%ten)

        n = n // ten
        n = n * ten

        zero += 1
    
    print(*r)