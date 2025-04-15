test = int(input())

for _ in range(test):
    m,a,b,c = map(int,input().split())

    row1 = row2 = m

    # seats left after monkey a allocation
    row1 = max(0,row1-a)

    # seats left after monkey b allocation
    row2 = max(0,row2-b)

    # seats left for c monkey
    seats_left = row1+row2

    seats_left = max(0,seats_left-c)

    # monkey seated  is total_seats - seats_left_after_monkey_allocation 
    print((2*m)-seats_left)


    