'''
https://leetcode.com/problems/count-servers-that-communicate/description/
'''

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        if row == 0 and col == 0:
            return 0

        connected = 0
        com_points = []
        com_row = [0] * row
        com_col = [0] * col

        for row_idx in range(row):
            for col_idx in range(col):
                if grid[row_idx][col_idx] == 1:
                    com_points.append((row_idx, col_idx))
                    com_row[row_idx] += 1
                    com_col[col_idx] += 1

        for row_idx, col_idx in com_points:
            if com_row[row_idx] > 1 or com_col[col_idx] > 1:
                connected += 1

        return connected


if __name__ == "__main__":
    sol =  Solution()
    
    test1 = sol.countServers(grid = [[1, 0], [0, 1]])
    assert test1 == 0
    
    test2 = sol.countServers(grid = [[1, 0], [1, 1]])
    assert test2 == 3
    
    test3 = sol.countServers(grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    assert test3 == 4
    