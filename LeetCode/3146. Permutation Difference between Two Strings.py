
def findPermutationDifference( s: str, t: str) -> int:
    s = {val:index for index,val in enumerate(s)}

    return sum([abs(index-s[val]) for index,val in enumerate(t)])


a = findPermutationDifference(s = "abcde", t = "edbac")
print(a)