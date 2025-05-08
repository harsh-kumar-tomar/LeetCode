import math
n = int(input())

odd_num = math.ceil(n/2)
even_num = math.floor(n/2)

print(even_num*(even_num+1) - odd_num*odd_num)