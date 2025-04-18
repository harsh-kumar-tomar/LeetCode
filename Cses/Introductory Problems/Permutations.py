import sys

n = int(sys.stdin.read())

odd = 1
even = 2
max_odd = n if n % 2 == 1 else n - 1
max_even = n if n % 2 == 0 else n - 1

odd_arr = []
even_arr = []


while odd <= max_odd:
    odd_arr.append(odd)
    odd += 2

while even <= max_even:
    even_arr.append(even)
    even += 2

arr1 = odd_arr + even_arr
arr2 = even_arr + odd_arr

possible_arr1 = True
possible_arr2 = True

for i in range(1,n):
    if abs(arr1[i-1] - arr1[i]) < 2:
        possible_arr1 = False
    
    if abs(arr2[i-1] - arr2[i]) < 2:
        possible_arr2 = False

print(*(arr1 if possible_arr1 else arr2)) if (possible_arr1 or possible_arr2) else print("NO SOLUTION")
