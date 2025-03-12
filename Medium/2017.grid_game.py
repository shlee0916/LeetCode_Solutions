'''
https://leetcode.com/problems/grid-game/description/?envType=daily-question&envId=2025-01-21
'''

import math

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = math.inf
        top_sum = sum(grid[0])
        bottom_sum = 0

        for idx in range(len(grid[0])):
            top_sum -= grid[0][idx]
            ans = min(ans, max(top_sum, bottom_sum))
            bottom_sum += grid[1][idx]

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.gridGame(grid = [[2, 5, 4], [1, 5, 1]])
    assert test1 == 4

    test2 = sol.gridGame(grid = [[3, 3, 1], [8, 5, 2]])
    assert test2 == 4

    test3 = sol.gridGame(grid = [[1, 3, 1, 15], [1, 3, 3, 1]])
    assert test3 == 7
