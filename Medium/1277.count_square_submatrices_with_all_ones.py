'''
https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
'''

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        table = [list(row) for row in matrix]

        row_len = len(matrix)
        col_len = len(matrix[0])

        for r_idx in range(1, row_len):
            for c_idx in range(1, col_len):
                if table[r_idx][c_idx]:
                    table[r_idx][c_idx] = 1 + min(table[r_idx - 1][c_idx],
                                                  table[r_idx - 1][c_idx - 1],
                                                  table[r_idx][c_idx - 1])

        return sum(sum(table, []))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countSquares(matrix =
                                    [
                                    [0, 1, 1, 1],
                                    [1, 1, 1, 1],
                                    [0, 1, 1, 1]
                                    ]
                                    )
    print(test1, 15)
    assert test1 == 15

    test2 = sol.countSquares(matrix = 
                                    [
                                    [1, 0, 1],
                                    [1, 1, 0],
                                    [1, 1, 0]
                                    ])
    print(test2, 7)
    assert test2 == 7
    