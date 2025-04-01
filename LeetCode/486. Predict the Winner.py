from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        hs = {}
        return self.recursion(nums, 0, len(nums) - 1, 0, 0, 0)

    def recursion(self,nums, start, end, turn, player1, player2,dp):

        if start > end:
            if player1 >= player2:
                return True
            else:
                return False

        if turn == 0:
            a = self.recursion(nums, start + 1, end, 1, player1 + nums[start], player2,dp)
            b = self.recursion(nums, start, end - 1, 1, player1 + nums[end], player2,dp)
        else:
            a = self.recursion(nums, start + 1, end, 0, player1, player2 + nums[start],dp)
            b = self.recursion(nums, start, end - 1, 0, player1, player2 + nums[end],dp)



"""
players can choose smaller element to limit the choices for the other player . 
And here optimally doesn't mean that both player will choose highest point .

If Player 1 has any possible path to win, the function returns True.

If all possible paths lead to a Player 2 win, the function returns False.
"""