s = input()

stack = []

for i in s:
    stack.append(i)

    if len(stack) >= 3 and stack[-1] == "B" and stack[-2] == "U" and stack[-3] == "W":
        stack.pop()
        stack.pop()
        stack.pop()

        if len(stack) >= 1 and stack[-1] != " ":
            stack.append(" ")

    
    

print("".join(stack).strip())