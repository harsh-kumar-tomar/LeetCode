from typing import *
from categories import Categories

path = Categories.BACKTRACK


def exist(board: List[List[str]], word: str) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                s = set()
                s.add((i, j))
                if recursion(i, j, board, s, 1, word, [(-1, 0), (1, 0), (0, -1), (0, 1)]):
                    return True
                s.remove((i, j))

    return False


def recursion(currentX: int, currentY: int, board: List[List[str]], usedCoordinates: Set, currentPointer: int,
              word: str, directions: List[Tuple[int, int]]):
    if currentPointer == len(word):
        return True

    for direction in directions:
        newX, newY = currentX + direction[0], currentY + direction[1]

        if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and (newX, newY) not in usedCoordinates and board[newX][
            newY] == word[currentPointer]:
            usedCoordinates.add((newX, newY))
            if recursion(newX, newY, board, usedCoordinates, currentPointer + 1, word, directions):
                return True
            usedCoordinates.remove((newX, newY))

    return False


a = exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
print(a)
