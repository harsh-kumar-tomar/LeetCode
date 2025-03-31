from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        return self.recursion(nums, 0, len(nums) - 1, 0, 0, 0)

    def recursion(self,nums, start, end, turn, player1, player2):

        if start > end:
            if player1 >= player2:
                return True
            else:
                return False

        if turn == 0:
            return self.recursion(nums, start + 1, end, 1, player1 + nums[start], player2) or self.recursion(nums, start, end - 1, 1, player1 + nums[end], player2)
        else:
            return self.recursion(nums, start + 1, end, 0, player1, player2 + nums[start]) and self.recursion(nums, start, end - 1, 0, player1, player2 + nums[end])



"""
players can choose smaller element to limit the choices for the other player . 
And here optimally doesn't mean that both player will choose highest point .

If Player 1 has any possible path to win, the function returns True.

If all possible paths lead to a Player 2 win, the function returns False.
"""