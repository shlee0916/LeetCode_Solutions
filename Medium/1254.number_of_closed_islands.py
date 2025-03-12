'''
https://leetcode.com/problems/number-of-closed-islands/description/
'''

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if grid[row][col] == 1:
                return True
                
            grid[row][col] = 1
            top = dfs(row - 1, col)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return top and bottom and right and left


        island = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and dfs(row, col):
                    island += 1
    
        return island


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.closedIsland(grid = [[1, 1, 1, 1, 1, 1, 1, 0], 
                                     [1, 0, 0, 0, 0, 1, 1, 0], 
                                     [1, 0, 1, 0, 1, 1, 1, 0], 
                                     [1, 0, 0, 0, 0, 1, 0, 1], 
                                     [1, 1, 1, 1, 1, 1, 1, 0]])
    assert test1 == 2

    test2 = sol.closedIsland(grid = [[0, 0, 1, 0, 0], 
                                     [0, 1, 0, 1, 0], 
                                     [0, 1, 1, 1, 0]])
    assert test2 == 1

    test3 = sol.closedIsland(grid = [[1, 1, 1, 1, 1, 1, 1], 
                                    [1, 0, 0, 0, 0, 0, 1], 
                                    [1, 0, 1, 1, 1, 0, 1], 
                                    [1, 0, 1, 0, 1, 0, 1], 
                                    [1, 0, 1, 1, 1, 0, 1], 
                                    [1, 0, 0, 0, 0, 0, 1], 
                                    [1, 1, 1, 1, 1, 1, 1]])
    assert test3 == 2
