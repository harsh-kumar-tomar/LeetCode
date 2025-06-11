import math

width , height , side = map(int,input().split())

calc = math.ceil(width/side)*math.ceil(height/side)
print(calc)