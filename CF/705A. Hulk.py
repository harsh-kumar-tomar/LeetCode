
n = int(input())

hate = "I hate"
love = "I love"
ls = []
flag = True

while n != 0:
    ls.append(hate if flag else love)
    flag = not flag
    n -= 1

r = " that ".join(ls)
print(r+" it")