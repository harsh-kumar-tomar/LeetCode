
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        i = j = 0

        players.sort()
        trainers.sort()

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
            j+= 1
        
        return count


a = Solution().matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8])
print(a)

"""
we want to distribute player as much as possible 
not to distribute trainer as much as possible 
"""