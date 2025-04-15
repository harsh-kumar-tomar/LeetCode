
test = int(input())

for _ in range(test):
    p = input()
    s = input()

    pointer_p = 0
    pointer_s = 0

    good = True

    while pointer_p < len(p) and pointer_s < len(s):
        count_p = 1
        count_s = 1

        char_p = p[pointer_p]
        pointer_p += 1
        while  pointer_p < len(p) and p[pointer_p] == char_p:
            count_p += 1
            pointer_p += 1
        
        char_s = s[pointer_s]
        pointer_s += 1
        while pointer_s < len(s) and s[pointer_s] == char_s:
            count_s += 1
            pointer_s += 1
        

        if count_s > 2*count_p or count_s < count_p or char_p != char_s :
            good = False
            break

        
    if pointer_p == len(p) and pointer_s == len(s):
        print("Yes") if good else print("No")
    else:
        print("No")
    
"""
tricky case 
p = "LR"
s = "LLRL"
this case could have crashed the code 
matching L of p to L of s , than matching R of p to R of s than break , this could give wrong ans "Yes"

tricky case 
p = "LRLR"
s = "LR"
len of p is greater than s
"""        

