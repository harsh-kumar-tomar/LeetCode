

def parseBoolExpr(expression: str) -> bool:

    stack = []

    for char in expression:

        if char == ")":

            count_t = 0
            count_f = 0

            while stack and stack[-1] != "(":
                temp = stack.pop()
                if temp == "f":
                    count_f += 1
                elif temp == "t":
                    count_t += 1

            # pop up (
            stack.pop()
            operation = stack.pop()
            result = ""

            if operation == "|":
                result = "t" if count_t!=0 else "f"
            elif operation == "&":
                result = "f" if count_f!=0 else "t"
            elif operation == "!":
                result = "f" if count_t!=0 else "t"

            stack.append(result)

        else:
            stack.append(char)


    return True if stack[-1] == "t" else False







a = parseBoolExpr(expression = "!(&(f,t))")
print(a)