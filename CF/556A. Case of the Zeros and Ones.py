n = int(input())

s = input()
stack = [s[0]]

for i in range(1,len(s)):

    if stack and ((stack[-1] == "1" and s[i] == "0") or (stack[-1] == "0" and s[i] == "1")):
        stack.pop()
    else:
        stack.append(s[i])

print(len(stack))