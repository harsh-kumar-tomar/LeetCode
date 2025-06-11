import math
a , b = map(int,input().split())
calc = a/b

if math.ceil(calc)-calc > calc - math.floor(calc):
    print(math.floor(calc))
else:
    print(math.ceil(calc))