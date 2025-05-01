from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        d= len(difficulty)
        w= len(worker)
        job = []

        for i in range(d):
            job.append((difficulty[i],profit[i]))
        
        job.sort()
        print(job)


        

        # r = []
        # for i in range(w):
        #     temp = float('-inf')
        #     for j in range(d):
        #         if worker[i] >= difficulty[j]:
        #             temp = max(temp,hash_map[difficulty[j]])
        #         else:
        #             break

        #     r.append(temp if temp != float('-inf') else 0)
        
        # return sum(r)





a = Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7])
print(a) 
"""
advice 
test case can contain duplicate values 
so dont use hash_map
"""

"""
Brute Force

d= len(difficulty)
        w= len(worker)
        r = []
        for i in range(w):
            temp = float('-inf')
            for j in range(d):
                if worker[i] >= difficulty[j]:
                    temp = max(temp,profit[j])

            r.append(temp if temp != float('-inf') else 0)
        
        return sum(r)
"""