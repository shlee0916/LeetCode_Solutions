'''
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
'''

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        row_limit = len(grid)
        col_limit = len(grid[0])
        next_points = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r_idx in range(row_limit):
            for c_idx in range(col_limit):

                if grid[r_idx][c_idx] > 0:
                    local_max = 0
                    stack = [(r_idx, c_idx)]
                    
                    while stack:
                        cur_r, cur_c = stack.pop()
                        local_max += grid[cur_r][cur_c]
                        grid[cur_r][cur_c] = 0

                        for delta_r, delta_c in next_points:
                            next_r = cur_r + delta_r
                            next_c = cur_c + delta_c

                            if (0 <= next_r < row_limit and
                                0 <= next_c < col_limit and
                                grid[next_r][next_c] > 0):

                                stack.append((next_r, next_c))

                    ans = max(ans, local_max)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMaxFish(grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]])
    assert test1 == 7

    test2 = sol.findMaxFish(grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    assert test2 == 1
    