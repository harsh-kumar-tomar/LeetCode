
test = int(input())

for _ in range(test):

    s = input()
    stack = [s[0]]

    for i in range(1,len(s)):
        char = s[i]

        if not stack:
            stack.append(char)
        else:
            top_element = stack.pop()
            if top_element == char or top_element == "0":
                stack = ["0"]
            else:
                stack.append(top_element)
                stack.append(char)


    print(len(stack))
