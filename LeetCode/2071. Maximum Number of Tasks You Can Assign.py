from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:

        tasks.sort()
        workers.reverse()
        count = 0
        i = j = 0

        while i < len(tasks) and j < len(workers) :
            temp_pills = 0
            while tasks[i] > workers[j] and pills > 0:
                workers[j] += 1*strength
                pills -= 1
                temp_pills += 1
            
            if tasks[i] <= workers[j]:
                count += 1
            else:
                pills += temp_pills
            
            i += 1
            j += 1

        return count


a = Solution().maxTaskAssign(tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5)
print(a)