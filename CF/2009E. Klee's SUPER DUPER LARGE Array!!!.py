test = int(input())

for _ in range(test):
    n , k = map(int,input().split())

    first_el = k
    last_el = n-1+k
    total_sum = (n*(first_el+last_el))//2
    right_sum = 0

    min_diff = float('inf')

    while last_el >= first_el:
        right_sum += last_el

        min_diff = min(min_diff,total_sum-2*right_sum)

        last_el -= 1

    print(min_diff)