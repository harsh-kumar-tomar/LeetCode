def lcs(p1, s1, p2, s2):
    if not s1 or not s2:
        return ""


def lengthOfLCS(p1, s1, p2, s2) -> int:
    if p1 == len(s1) or p2 == len(s2):
        return 0

    if s1[p1] == s2[p2]:
        temp = 1 + lengthOfLCS(p1 + 1, s1, p2 + 1, s2)
        return temp
    else:
        temp1 = lengthOfLCS(p1 + 1, s1, p2, s2)
        temp2 = lengthOfLCS(p1, s1, p2 + 1, s2)
        return temp1 if temp1 > temp2 else temp2


if __name__ == "__main__":
    a = lengthOfLCS(0, "pokemon", 0, "pikachu")
    print(a)
    # a = "po"
    # print(len(a))