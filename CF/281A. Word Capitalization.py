s = input()

if 97<= ord(s[0]) <=122:
    temp = ord(s[0])-32    
    print(chr(temp)+s[1:])
else:
    print(s)
