'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
'''

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        target = len(grid) - 1

        if grid[0][0] == 1 or grid[target][target] == 1:
            return -1

        que = deque([((0, 0), 1)])
        grid[0][0] = 1
        while que:
            (cur_row, cur_col), path_len = que.popleft()

            if cur_row == target and cur_col == target:
                return path_len

            next_pos = [(cur_row - 1, cur_col - 1),
                        (cur_row - 1, cur_col),
                        (cur_row - 1, cur_col + 1),
                        (cur_row, cur_col - 1),
                        (cur_row, cur_col + 1),
                        (cur_row + 1, cur_col - 1),
                        (cur_row + 1, cur_col),
                        (cur_row + 1, cur_col + 1)]

            for next_x, next_y in next_pos:
                if 0 <= next_x <= target and 0 <= next_y <= target:
                    if grid[next_x][next_y] == 0:
                        grid[next_x][next_y] = 1
                        que.append(((next_x, next_y), path_len + 1))

        return -1
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.shortestPathBinaryMatrix(grid = [[0, 1], [1, 0]])
    assert test1 == 2

    test2 = sol.shortestPathBinaryMatrix(grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]])
    assert test2 == 4

    test3 = sol.shortestPathBinaryMatrix(grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]])
    assert test3 == -1
    