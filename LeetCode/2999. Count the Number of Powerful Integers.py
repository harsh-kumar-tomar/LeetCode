


def numberOfPowerfulInt( start: int, finish: int, limit: int, s: str) -> int:

    if len(str(finish)) < limit:
        return 0
    
    def recursion(temp):

        if len(temp) == limit:
            if start <= int(temp) <= finish:
                count[0] += 1
                ans.append(temp)
            return

        for i in range(0,limit+1):
            recursion(str(i)+temp)

        
    count = [0]
    ans =[]
    
    recursion(s)
    print(ans)
    return count[0]



a = numberOfPowerfulInt(start = 15, finish = 215, limit = 6, s = "10")
print(a)