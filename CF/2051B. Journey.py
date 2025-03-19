
test = int(input())


for i in range(test):
    n, arr = input().split(maxsplit=1)
    distance_to_cover = int(n)
    arr = list(map(int, arr.split()))


    days_covered = (distance_to_cover // sum(arr))*3
    distance_covered = (distance_to_cover // sum(arr))*sum(arr)
    pointer = 0



    while distance_covered < distance_to_cover:
        if pointer == len(arr):
            pointer = 0

        distance_covered += arr[pointer]
        days_covered += 1

        pointer += 1


    print(days_covered)
