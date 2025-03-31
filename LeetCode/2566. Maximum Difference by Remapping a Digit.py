
def minMaxDifference(num: int) -> int:
    num = list(str(num))

    max_num = num.copy()
    min_num = num.copy()

    temp = "#"

    for index, el in enumerate(max_num):
        if el == temp:
            max_num[index] = "9"

        if temp == "#" and el != "9":
            temp = el
            max_num[index] = "9"

    temp = "#"

    for index, el in enumerate(min_num):
        if el == temp:
            min_num[index] = "0"

        if temp == "#" and el != "0":
            temp = el
            min_num[index] = "0"

    return int("".join(max_num)) - int("".join(min_num))


a = minMaxDifference(num = 90)
print(a)