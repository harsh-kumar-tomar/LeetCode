import sys

word = sys.stdin.read().strip()
n = len(word)
char = word[0]
max_count = 0
count = 1
curr_pointer = 1

while curr_pointer <= n:

    if curr_pointer == n:
        max_count = max(max_count,count)
        break
    
    if word[curr_pointer] == char:
        count += 1
    else:
        max_count = max(max_count,count)
        count = 1
        char = word[curr_pointer]
    
    curr_pointer += 1

print(max_count)



