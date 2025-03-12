'''
https://leetcode.com/problems/valid-sudoku/?source=submission-noac
'''

from typing import List


class Solution:
    def __is_valid(self, unit):
        unit = [num for num in unit if num != "."]

        return len(set(unit)) == len(unit)


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_valid = True
        for row in board:
            if not self.__is_valid(row):
                row_valid = False
                break

        col_valid = True
        for col in zip(*board):
            if not self.__is_valid(col):
                col_valid = False
                break

        square_valid = True
        for row_idx in (0, 3, 6):
            for col_idx in (0, 3, 6):
                square = [board[r_idx][c_idx] for r_idx in range(row_idx, row_idx + 3) for c_idx in range(col_idx, col_idx + 3)]
                if not self.__is_valid(square):
                    square_valid = False
                    break

        return row_valid and col_valid and square_valid


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isValidSudoku(board = 
                                    [["5","3",".",".","7",".",".",".","."]
                                    ,["6",".",".","1","9","5",".",".","."]
                                    ,[".","9","8",".",".",".",".","6","."]
                                    ,["8",".",".",".","6",".",".",".","3"]
                                    ,["4",".",".","8",".","3",".",".","1"]
                                    ,["7",".",".",".","2",".",".",".","6"]
                                    ,[".","6",".",".",".",".","2","8","."]
                                    ,[".",".",".","4","1","9",".",".","5"]
                                    ,[".",".",".",".","8",".",".","7","9"]])
    assert test1 == True
    
    test2 = sol.isValidSudoku(board = 
                                    [["8","3",".",".","7",".",".",".","."]
                                    ,["6",".",".","1","9","5",".",".","."]
                                    ,[".","9","8",".",".",".",".","6","."]
                                    ,["8",".",".",".","6",".",".",".","3"]
                                    ,["4",".",".","8",".","3",".",".","1"]
                                    ,["7",".",".",".","2",".",".",".","6"]
                                    ,[".","6",".",".",".",".","2","8","."]
                                    ,[".",".",".","4","1","9",".",".","5"]
                                    ,[".",".",".",".","8",".",".","7","9"]])
    assert test2 == False
    