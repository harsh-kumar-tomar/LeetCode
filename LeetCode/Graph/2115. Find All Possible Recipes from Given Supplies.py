from typing import List


def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

    s = set()
    r = []

    for el in supplies:
        s.add(el)

    i = 0

    while i < 2:

        for index,ingredient in enumerate(ingredients):
            flag = True
            for item in ingredient:
                if item not in s:
                    flag = False
                    break
            if flag:
                s.add(recipes[index])

        i += 1

    for index, ingredient in enumerate(ingredients):
        flag = True
        for item in ingredient:
            if item not in s:
                flag = False
                break
        if flag:
            r.append(recipes[index])

    return r



a = findAllRecipes( recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"])
print(a)