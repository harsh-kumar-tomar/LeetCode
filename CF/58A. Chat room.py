s = input()

text = "hello"
curr_pointer = 0

i = 0

while i < len(s) and curr_pointer < len(text):

    if s[i] == text[curr_pointer]:
        curr_pointer += 1
    
    i += 1

print("YES") if curr_pointer == len(text) else print("NO")



