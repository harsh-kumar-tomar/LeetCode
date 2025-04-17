
def numDecodings( s: str) -> int:

    
    def recursion(curr ,temp:list[int]):

        if curr == len(s):
            count.add("".join(temp))
            return
    
        # choose 1 char 
        char = number_to_letter[s[curr]]
        if char in number_to_letter:
            temp.append(char)
            recursion(curr+1,temp)
        
        # choose 2 char
        char = number_to_letter[s[curr]+s[curr+1]]
        if char in number_to_letter:
            temp.append(char)
            recursion(curr+2,temp)

    count = set()
    number_to_letter = {str(i): chr(64 + i) for i in range(1, 27)}
    recursion(0,[])
    print(count)


a = numDecodings("12")
print(a)