'''
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
'''

from heapq import heappop, heappush

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        row_limit = len(grid)
        col_limit = len(grid[0])

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        heap = [(0, 0, 0)]
        visit = set()
        while heap:
            cost, x, y = heappop(heap)

            if (x, y) == (row_limit - 1, col_limit - 1):
                return cost

            if (x, y) in visit:
                continue
            visit.add((x, y))

            for num, (delta_x, delta_y) in enumerate(directions):
                next_x = x + delta_x
                next_y = y + delta_y

                if 0 <= next_x < row_limit and 0 <= next_y < col_limit and (next_x, next_y) not in visit:
                    if grid[x][y] == num + 1:
                        heappush(heap, (cost, next_x, next_y))
                    else:
                        heappush(heap, (cost + 1, next_x, next_y))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minCost(grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]])
    assert test1 == 3

    test2 = sol.minCost(grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]])
    assert test2 == 0

    test3 = sol.minCost(grid = [[1, 2], [4, 3]])
    assert test3 == 1
    