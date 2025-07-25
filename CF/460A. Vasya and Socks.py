n , m = map(int,input().split())

days = n 
calc = n // m

while calc != 0:
    days += calc
    calc = calc // m

print(days) 