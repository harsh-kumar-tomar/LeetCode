problems , meet_time = map(int,input().split())

total_time = 240
time_left = total_time - meet_time

count_problems = 0
i = 1
time_taken = 0

while i <= problems and time_taken + 5*i <= time_left:
    time_taken += 5*i 
    count_problems += 1
    i += 1

print(count_problems)


"""
without binary search
problems , meet_time = map(int,input().split())

total_time = 240
time_left = total_time - meet_time

count_problems = 0
i = 1
time_taken = 0

while i <= problems and time_taken + 5*i <= time_left:
    time_taken += 5*i 
    count_problems += 1
    i += 1

print(count_problems)
"""