'''
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
'''

from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]

        for x, y in guards + walls:
            grid[x][y] = 1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in guards:
            for dx, dy in dirs:
                new_x = x
                new_y = y
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and grid[new_x + dx][new_y + dy] != 1:
                    new_x += dx
                    new_y += dy
                    grid[new_x][new_y] = 2

        return sum(row.count(0) for row in grid)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countUnguarded(m = 4, n = 6, guards = [[0, 0], [1, 1], [2, 3]], walls = [[0, 1], [2, 2], [1, 4]])
    assert test1 == 7

    test2 = sol.countUnguarded(m = 3, n = 3, guards = [[1, 1]], walls = [[0, 1], [1, 0], [2, 1], [1, 2]])
    assert test2 == 4
    