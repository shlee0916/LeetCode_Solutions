'''
https://leetcode.com/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
'''

from collections import deque

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 

        row_limit = len(board)
        col_limit = len(board[0])
        if row_limit <= 2 or col_limit <= 2:
            return 

        que = deque()
        for row in range(row_limit):
            que.extend([(row, 0), (row, col_limit - 1)])

        for col in range(col_limit):
            que.extend([(0, col), (row_limit - 1, col)])

        while que:
            row, col = que.popleft()

            if 0 <= row < row_limit and 0 <= col < col_limit and board[row][col] == "O":
                board[row][col] = "N"
                que.extend([(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)])

        for row in range(row_limit):
            for col in range(col_limit):
                if board[row][col] == "N":
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1_board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    test1 = sol.solve(board = test1_board)
    assert test1_board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    test2_board = [["X"]]
    test2 = sol.solve(board = test2_board)
    assert test2_board == [["X"]]
    