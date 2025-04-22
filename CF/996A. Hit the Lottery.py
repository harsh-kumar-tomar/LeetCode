
n = int(input())
notes = [1,5,10,20,100]
count = 0
for i in range(len(notes)-1,-1,-1):
    count += n//notes[i]
    n = n % notes[i]

print(count)

"""

Appraoch 1
dp = [float('inf')]*(n+1)
dp[0] = 0

for  i in range(1,n+1):
    for note in notes:
        if i - note >= 0:
            dp[i] =min(dp[i] , 1 + dp[i-note])


Approach 1
dp = {}
def min_bill(n):
    if n < 0:
        return float('inf')

    if n == 0:
        return 0
    
    if n in dp:
        return dp[n]
    
    count = float('inf')
    for note in notes:
        temp = 1+ min_bill(n-note)
        count = min(count,temp)
    
    dp[n] = count

    return dp[n]
"""