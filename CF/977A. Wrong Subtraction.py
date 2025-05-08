n , k = map(int,input().split())

while k > 0:
    rem = n % 10

    if n < 10:
        n -= 1
        k -= 1
    if rem == 0:
        n = n // 10
        k -= 1
    else:
        n -= min(k,rem)
        k -= rem
print(n)

