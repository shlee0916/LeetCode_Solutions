'''
https://leetcode.com/problems/path-with-minimum-effort/description/?envType=daily-question&envId=2023-11-16
'''

from heapq import heappush, heappop

from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_limit = len(heights)
        col_limit = len(heights[0])

        efforts = [[float("inf")] * col_limit for _ in range(row_limit)]
        efforts[0][0] = 0

        next_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        heap = [(0, 0, 0)]
        while heap:
            effort, x, y = heappop(heap)

            if x == row_limit - 1 and y == col_limit - 1:
                return effort

            for delta_x, delta_y in next_directions:
                new_x = x + delta_x
                new_y = y + delta_y

                if 0 <= new_x < row_limit and 0 <= new_y < col_limit:
                    new_effort = max(effort, abs(heights[new_x][new_y] - heights[x][y]))

                    if efforts[new_x][new_y] > new_effort:
                        efforts[new_x][new_y] = new_effort
                        heappush(heap, (new_effort, new_x, new_y))

        # return efforts[row_limit - 1][col_limit - 1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minimumEffortPath(heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]])
    assert test1 == 2

    test2 = sol.minimumEffortPath(heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]])
    assert test2 == 1

    test3 = sol.minimumEffortPath(heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]])
    assert test3 == 0
    