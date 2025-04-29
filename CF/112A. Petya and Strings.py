def give_index(num:int):

    if 65 <= num <= 90:
        return  num - 65 + 1
    else:
        return  num - 97 + 1


s1 = input()
s2 = input()

n = len(s1)
result = 0

for i in range(0,n):
    char1 = ord(s1[i])
    char2 = ord(s2[i])

    if give_index(char1) > give_index(char2):
        result = 1
        break
    elif give_index(char1) < give_index(char2):
        result = - 1
        break

print(result)


