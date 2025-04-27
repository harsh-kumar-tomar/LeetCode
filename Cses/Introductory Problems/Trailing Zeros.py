
n = int(input())
five = 5
power = 1
count_fives = 0

while  n // (5**power) != 0:

    count_fives += n // (5**power)
    power += 1

print(count_fives)

"""
change question to count no of 5 appearing in every digit 
for every zero we need one 2 and one 5 , we have so many two (even numebrs ) so we need 
to count no of 5 which are limited .
here we are dividing first by 5 , 25 , 100 
"""