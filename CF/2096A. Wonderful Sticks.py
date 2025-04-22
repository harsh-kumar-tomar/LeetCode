
test = int(input())

for _ in range(test):
    n = int(input())
    s = input()
    s.replace('<','D')
    s.replace('>','I')
    pattern = s
    stack = [1]
    num = 2
    pattern_ls = list(pattern)


    for index,char in enumerate(pattern):

        if char == "I":
            stack.append(num)
        else:
            ls = []
            temp_pointer = index-1

            while temp_pointer >= 0 and pattern_ls[temp_pointer] != "I":
                temp = stack.pop()
                ls.append(temp)
                temp_pointer -= 1 
            
            increase = stack.pop()
            stack.append(num)
            stack.append(increase)
            stack.extend(reversed(ls))    

        num += 1



    print("".join(list(map(str,stack))))
