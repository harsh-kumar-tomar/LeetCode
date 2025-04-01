
def decodeString(s: str) -> str:

    stack = []

    for index, char in enumerate(s):

        if char == "]":
            temp = []
            num = []

            while stack[-1] != "[":
                temp.append(stack.pop())

            stack.pop()
            temp.reverse()

            while stack and stack[-1] in "0123456789"  :
                num.append(stack.pop())

            num.reverse()
            num = int("".join(num))

            temp = temp*num
            stack.append("".join(temp))

        else:
            stack.append(char)

    return "".join(stack)


a = decodeString( "2[abc]3[cd]ef")
print(a)