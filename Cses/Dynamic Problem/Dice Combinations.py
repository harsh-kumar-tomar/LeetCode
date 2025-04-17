import sys
import math
sys.setrecursionlimit(1000000)  
MOD = 10**9+7

def recursion(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1,n+1):
        for j in range(1,7):
            if i - j >= 0:
                dp[i] += (dp[i-j])%MOD
    
    return dp[n]

    
        
# dp = {}
# def recursion(n):
#     if n < 0 :
#         return 0
    
#     if n == 0:
#         return 1
    
#     if n in dp:
#         return dp[n]
    
#     count = 0
#     for i in range(1,7):
#         count += recursion(n-i)
    
#     dp[n] = count

#     return dp[n]   

n = int(input())
print(recursion(n)%(10**9+7))

