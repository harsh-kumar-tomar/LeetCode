
test = int(input())
for _ in range(test):
    s = input().split()

    result = []
    for word in s:
        result.append(word[0])
    
    print("".join(result))
