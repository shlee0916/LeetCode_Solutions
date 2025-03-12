'''
https://leetcode.com/problems/number-of-enclaves/description/
'''

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        new_direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

        stack = []
        for idx, num in enumerate(grid[0]):
            if num == 1:
                stack.append((0, idx))
        
        for idx, num in enumerate(grid[-1]):
            if num == 1:
                stack.append((rows - 1, idx))

        for row in range(rows):
            if grid[row][0] == 1:
                stack.append((row, 0))
            if grid[row][cols - 1] == 1:
                stack.append((row, cols - 1))
        
        while stack:
            row, col = stack.pop()
            grid[row][col] = 0

            for row_delta, col_delta in new_direction:
                new_row = row + row_delta
                new_col = col + col_delta
                
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    stack.append((new_row, new_col))


        return sum(row.count(1) for row in grid)
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numEnclaves(grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    assert test1 == 3

    test2 = sol.numEnclaves(grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
    assert test2 == 0
