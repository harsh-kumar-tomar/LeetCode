num = list(map(int,input()))

curr_pointer = len(num)-1
steps = 0
sum_num = 0

while curr_pointer != -1:
    num[curr_pointer] = (num[curr_pointer]- sum_num)%10

    steps += num[curr_pointer] + 1
    
    sum_num += num[curr_pointer]

    num.pop()

    curr_pointer -= 1

print(steps)

