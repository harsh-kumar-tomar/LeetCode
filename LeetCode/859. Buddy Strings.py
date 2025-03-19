def buddyStrings(s: str, goal: str) -> bool:

    if len(s) != len(goal):
        return False

    if s == goal:
        hash = {}
        for  char in s:
            if char in hash:
                hash[char] += 1
            else:
                hash[char] = 1

        for value in hash.values():
            if value == 2:
                return True

        return False

    n = len(s)
    countDiff = 0
    l1 = []
    l2 = []

    for i in range (n):
        if s[i] != goal[i]:
            countDiff += 1
            l1.append(s[i])
            l2.append(goal[i])

    if countDiff == 2:
        if l1[0] == l2[1] and l1[1] == l2[0]:
            return True
        return False

    return False


a = buddyStrings(s = "abcd", goal = "cbad")
print(a)

