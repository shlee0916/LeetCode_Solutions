'''

'''

from heapq import heappush, heappop
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        visit = set([0, 0])
        heap = []

        water_level, cur_x, cur_y = grid[0][0], 0, 0
        res = water_level
        while (cur_x, cur_y) != (size - 1, size - 1):
            for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = cur_x + delta_x
                new_y = cur_y + delta_y
                if 0 <= new_x < size and 0 <= new_y < size and (new_x, new_y) not in visit:
                    heappush(heap, (grid[new_x][new_y], new_x, new_y))
                    visit.add((new_x, new_y))

            water_level, cur_x, cur_y = heappop(heap)
            res = max(res, water_level)

        return res


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.swimInWater(grid = [[0, 2], [1, 3]])
    assert test1 == 3
    
    test2 = sol.swimInWater(grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]])
    assert test2 == 16
    