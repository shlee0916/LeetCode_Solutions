'''
https://leetcode.com/problems/game-of-life/description/
'''

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_limit = len(board)
        col_limit = len(board[0])

        def check_neighbors(x: int, y: int):
            neighbors = []
            for delta_x in range(-1, 2):
                new_x = x + delta_x
                for delta_y in range(-1, 2):
                    new_y = y + delta_y
                    if (new_x, new_y) != (x, y):
                        if 0 <= new_x < row_limit and 0 <= new_y < col_limit:
                            neighbors.append((new_x, new_y))
            
            cnt = 0
            for new_x, new_y in neighbors:
                if board[new_x][new_y] == 1:
                    cnt += 1

            return cnt

        step = {}
        for x in range(row_limit):
            for y in range(col_limit):
                neighbors = check_neighbors(x, y)

                if board[x][y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        step[(x, y)] = 0
                else:
                    if neighbors == 3:
                        step[(x, y)] = 1

        for (x, y), value in step.items():
            board[x][y] = value


if __name__ == "__main__":
    sol = Solution()

    board1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    test1 = sol.gameOfLife(board = board1)
    assert board1 == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    board2 = [[1, 1], [1, 0]]
    test2 = sol.gameOfLife(board2)
    assert board2 == [[1, 1], [1, 1]]
    