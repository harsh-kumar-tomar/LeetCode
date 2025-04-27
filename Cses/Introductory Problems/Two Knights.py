import math
n = int(input())

for i in range(1,n+1):
    print(math.comb(i*i,2)-4*(i-1)*(i-2))


"""
approach
total possible combination - all the positions where knight will attack on each other
so total combination is 
    n*nC2 
basically total position whic is n*n taking 2 at a time . so n2 C 2

and all the position where knight will attack on each other .
for knight to attack we need a 2*3 block or 3*2 block .
and for each block knight can attack in 2 ways for 2*3 block and 2 ways for 3*2 blocks

so now task is to find no of 2*3 blocks and 3*2 blocks in n*n board.

lets suppose we have 4*4 board 
and lets consider only 2 from 2*3 

1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

so we need to find out no of 2 blocks in Y directions , which is 3 
as (1,5),(5,9),(9,13) so n - 1 block are there for 2 blocks 

for 3 
we will take as (1,2,3) , (2,3,4) which is 2 
so are there n-2 blocks for 3

so no of 2*3 blocks in 4*4 
are (n-1)*(n-2) so total attacks are 2*(n-1)*(n-2)

and no of 3*2 blocks in 4*4
are (n-2)*(n-1) so tatal attacks are 2*(n-2)*(n-1)

so total is 4*(n-1)*(n-2)

"""