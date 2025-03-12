'''
https://leetcode.com/problems/rotting-oranges/
'''

from collections import deque

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_limit = len(grid)
        col_limit = len(grid[0])

        fresh_point = 0
        rot_point = deque()
        for row in range(row_limit):
            for col in range(col_limit):
                if grid[row][col] == 1:
                    fresh_point += 1
                elif grid[row][col] == 2:
                    rot_point.append((row, col))

        mins = 0
        while rot_point and fresh_point > 0:
            mins += 1

            for _ in range(len(rot_point)):
                cur_x, cur_y = rot_point.popleft()

                for delta_x, delta_y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    next_x = cur_x + delta_x
                    next_y = cur_y + delta_y
                    
                    if 0 <= next_x < row_limit and 0 <= next_y < col_limit:
                        if grid[next_x][next_y] == 1:
                            fresh_point -= 1
                            grid[next_x][next_y] = 2
                            rot_point.append((next_x, next_y))

        return mins if fresh_point == 0 else -1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.orangesRotting(grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    assert test1 == 4

    test2 = sol.orangesRotting(grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    assert test2 == -1

    test3 = sol.orangesRotting(grid = [[0 ,2]])
    assert test3 == 0
    