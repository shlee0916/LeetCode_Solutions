'''
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
'''

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_len = len(grid)
        col_len = len(grid[0])

        rows = []
        cols = []

        for row in grid:
            rows.append(2 * sum(row) - row_len)

        for col in zip(*grid):
            cols.append(2 * sum(col) - col_len)

        diff = []
        for row_idx in range(row_len):
            new_row = []
            for col_idx in range(col_len):
                new_row.append(rows[row_idx] + cols[col_idx])
            diff.append(new_row)

        return diff


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.onesMinusZeros(grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]])
    assert test1 == [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
    
    test2 = sol.onesMinusZeros(grid = [[1, 1, 1], [1, 1, 1]])
    assert test2 == [[5, 5, 5], [5, 5, 5]]
    