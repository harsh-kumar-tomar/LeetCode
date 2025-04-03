from collections import deque


def decodeString(s: str) -> str:

    stack = []

    for index, char in enumerate(s):

        if char == "]":
            temp = deque()
            num = deque()

            while stack[-1] != "[":
                temp.appendleft(stack.pop())

            stack.pop()

            while stack and stack[-1].isdigit()  :
                num.appendleft(stack.pop())

            num = int("".join(num))

            temp = temp*num
            stack.append("".join(temp))

        else:
            stack.append(char)

    return "".join(stack)


a = decodeString( "2[abc]3[cd]ef")
print(a)