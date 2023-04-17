'''
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
'''

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])

        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                row_max[row_idx] = max(row_max[row_idx], grid[row_idx][col_idx])
                col_max[col_idx] = max(col_max[col_idx], grid[row_idx][col_idx])

        result = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                result += min(row_max[row_idx], col_max[col_idx]) - grid[row_idx][col_idx]

        return result
    
    # I think it's not good for readability..
    def maxIncreaseKeepingSkyline_oneline(self, grid: List[List[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        return sum(min(row_max[row], col_max[col]) for row in range(len(grid)) for col in range(len(grid[0]))) - sum(map(sum, grid))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxIncreaseKeepingSkyline(grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
    assert test1 == 35

    test2 = sol.maxIncreaseKeepingSkyline(grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert test2 == 0
