'''
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
'''

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        cur_row = row - 1
        cur_col = 0
        cnt = 0
        while cur_row >= 0 and cur_col < col:
            if grid[cur_row][cur_col] < 0:
                cnt += col - cur_col
                cur_row -= 1
            else:
                cur_col += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.countNegatives(grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
    assert test1 == 8
    
    test2 = sol.countNegatives(grid = [[3, 2], [1, 0]])
    assert test2 == 0
    