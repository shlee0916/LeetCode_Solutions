'''
https://leetcode.com/problems/island-perimeter/description/
'''

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for r_idx, r_val in enumerate(grid):
            for c_idx, c_val in enumerate(r_val):
                perimeter += 4 * c_val
                if r_idx > 0:
                    perimeter -= c_val * grid[r_idx - 1][c_idx]
                if r_idx < len(grid) - 1:
                    perimeter -= c_val * grid[r_idx + 1][c_idx]
                if c_idx > 0:
                    perimeter -= c_val * grid[r_idx][c_idx - 1]
                if c_idx < len(grid[0]) - 1:
                    perimeter -= c_val * grid[r_idx][c_idx + 1]

        return perimeter


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.islandPerimeter(grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
    print(test1, 16)
    assert test1 == 16
    
    test2 = sol.islandPerimeter(grid = [[1]])
    print(test2, 4)
    assert test2 == 4
    
    test3 = sol.islandPerimeter(grid = [[1, 0]])
    print(test3, 4)
    assert test3 == 4
    