from typing import *


def maxCompatibilitySum(students: List[List[int]], mentors: List[List[int]]) -> int:
    r = 0
    recursion(students,mentors,set(),set(),set(),r)
    return r



def recursion(students:List[List[int]],mentors:List[List[int]], usedStudent:Set, usedMentor:Set ,pair:Set, r:int):

    if len(pair) == len(students):
        count = 0
        for i,j in pair:
            count += compatibility(students[i],mentors[j])
        r = max(r,count)
        return


    for i in range (len(students)):
        for j  in range (len(mentors)):
            if i not in usedStudent and j not in usedMentor:
                usedStudent.add(i)
                usedMentor.add(j)
                pair.add((i,j))
                recursion(students,mentors,usedStudent,usedMentor,pair,r)
                pair.remove((i,j))
                usedStudent.remove(i)
                usedMentor.remove(j)

def compatibility(student:List[int],mentor:List[int]):
    n = len(student)
    count = 0

    for i in range (n):
        if student[i] == mentor[i]:
            count += 1

    return count






a = maxCompatibilitySum(students = [[0,1,0,1,1,1],[1,0,0,1,0,1],[1,0,1,1,0,0]], mentors = [[1,0,0,0,0,1],[0,1,0,0,1,1],[0,1,0,0,1,1]])
print(a)