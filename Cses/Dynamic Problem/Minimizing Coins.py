import sys

input = sys.stdin.readline

num , x = map(int,input().split())
coins = list(map(int,input().split()))

n = x
dp = [10**9]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i],1+dp[i-coin])

print(dp[n] if dp[n] != 10**9 else -1)




"""
theoretically 
min_coin(n) should return the min coin  we need to form n 

approach 1

dp = {}

def min_coin(n) :
    if n == 0:
        return 0

    if n < 0:
        return float('inf')

    if n in dp :
        return dp[n]
    
    count = float('inf')

    for coin in coins:
        way = 1+min_coin(n-coin)
        count = min(count,way)
    
    dp[n] = count

    return dp[n]


"""