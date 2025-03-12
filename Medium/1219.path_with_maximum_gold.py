'''
https://leetcode.com/problems/path-with-maximum-gold/?envType=daily-question&envId=2024-05-14
'''

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row_limit = len(grid)
        col_limit = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            local_ans = 0
            if 0 <= row < row_limit and 0 <= col < col_limit and grid[row][col] != 0:
                org_gold = grid[row][col]
                grid[row][col] = 0

                for row_delta, col_delta in directions:
                    local_ans = max(local_ans, dfs(row + row_delta, col + col_delta))

                grid[row][col] = org_gold
                local_ans += org_gold

            return local_ans

        ans = 0
        for row in range(row_limit):
            for col in range(col_limit):
                ans = max(ans, dfs(row, col))

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getMaximumGold(grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]])
    assert test1 == 24

    test2 = sol.getMaximumGold(grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])
    assert test2 == 28
    