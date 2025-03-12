'''
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/?envType=daily-question&envId=2024-10-30
'''

from functools import cache

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row_limit = len(grid)
        col_limit = len(grid[0])
        directions = [(-1, 1), (0, 1), (1, 1)]
        
        @cache
        def dp(row_idx, col_idx):
            ans = 0

            for delta_row, delta_col in directions:
                nrow_idx = row_idx + delta_row
                ncol_idx = col_idx + delta_col

                if 0 <= nrow_idx < row_limit and ncol_idx < col_limit and grid[row_idx][col_idx] < grid[nrow_idx][ncol_idx]:
                    ans = max(ans, 1 + dp(nrow_idx, ncol_idx))
                    
            return ans

        return max(dp(ridx, 0) for ridx in range(row_limit))
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxMoves(grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
    assert test1 == 3

    test2 = sol.maxMoves(grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]])
    assert test2 == 0
