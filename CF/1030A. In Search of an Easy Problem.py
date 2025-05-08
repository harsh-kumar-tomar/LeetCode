n = int(input())

arr = list(map(int,input().split()))

easy = True
for i in arr:
    if i  == 1:
        easy = False

print("EASY") if easy else print("HARD")