import sys

test = 1

for _ in range(test):
    n, k = 5,2
    arr = 4,2,3,1,3

    max_index1 = -1
    max_index2 = -1

    for index, val in enumerate(arr):

        if max_index1 == -1 or  val > arr[max_index1]:
            max_index2 = max_index1
            max_index1 = index

        elif (val > arr[max_index2]  and max_index1 != max_index2) or max_index2 == -1 :
            max_index2 = index

    print(max_index1,max_index2)
