'''
https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28
'''

from heapq import heappush, heappop
from collections import defaultdict

from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_map = defaultdict(list)
        for idx, query in enumerate(queries):
            query_map[query].append(idx)
        queries.sort()
        
        ans = [0] * len(queries)

        row_limit = len(grid)
        col_limit = len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        heap = [(grid[0][0], 0, 0)]
        cur_point = 0
        visited = {(0, 0)}
        
        for query in queries:
            while heap and heap[0][0] < query:
                cur_cell, cur_x, cur_y = heappop(heap)

                if cur_cell < query:
                    cur_point += 1

                    for dx, dy in dirs:
                        next_x = cur_x + dx
                        next_y = cur_y + dy

                        if 0 <= next_x < row_limit and 0 <= next_y < col_limit and (next_x, next_y) not in visited:
                            heappush(heap, (grid[next_x][next_y], next_x, next_y))
                            visited.add((next_x, next_y))

            for idx in query_map[query]:
                ans[idx] = cur_point

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxPoints(grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]], queries = [5,6,2])
    assert test1 == [5, 8, 1]

    test2 = sol.maxPoints(grid = [[5, 2, 1], [1, 1, 2]], queries = [3])
    assert test2 == [0]
    