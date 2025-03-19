countIngredient, magicPowder = map(int,input().split())

cookieIngredientList = list(map(int,input().split()))
currentIngredientList = list(map(int,input().split()))

n = len(cookieIngredientList)
pointer = 0
countCookie = 0
fount = False
while True:
    for i in range(n):
        if currentIngredientList[i] >= cookieIngredientList[i]:
            currentIngredientList[i] -= cookieIngredientList[i]
        else:
            diff = cookieIngredientList[i] - currentIngredientList[i]
            if diff <= magicPowder:
                currentIngredientList[i] += diff
                currentIngredientList[i] -= cookieIngredientList[i]

                magicPowder -= diff
            else:
                fount = True
                print(countCookie)
                break
    if fount:
        break
    countCookie += 1


print(countCookie)
