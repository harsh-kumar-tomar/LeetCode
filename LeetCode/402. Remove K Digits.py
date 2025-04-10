def removeKdigits(num: str, k: int) -> str:
    stack = [num[0]]
    n = len(num)

    for index in range(1, n):

        el = num[index]

        if not stack or stack[-1] == el or stack[-1] < el:
            stack.append(el)
        elif stack[-1] >= el:
            while stack and stack[-1] > el and k > 0:
                k -= 1
                stack.pop()
            stack.append(el)

        if k == 0:
            stack.append(num[index + 1 :])
            break

    stack = stack[: len(stack) - k]
    r = ''.join(stack).lstrip('0')

    return "0" if not r else r



a = removeKdigits(num="112", k=1)
print(a)
