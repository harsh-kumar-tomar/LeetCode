width , height = map(int,input().split())

calc = (width//2)*height + ((width%2)*height)//2

print(calc)