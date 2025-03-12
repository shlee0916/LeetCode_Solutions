'''
https://leetcode.com/problems/as-far-from-land-as-possible/
'''

from collections import deque

from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row_limit = len(grid)
        col_limit = len(grid[0])

        que = deque()
        for r_idx in range(row_limit):
            for c_idx in range(col_limit):
                if grid[r_idx][c_idx] == 1:
                    que.append((r_idx, c_idx))

        dist = 0
        visit = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while que:
            for _ in range(len(que)):
                cur_x, cur_y = que.popleft()

                for delta_x, delta_y in directions:
                    new_x = cur_x + delta_x
                    new_y = cur_y + delta_y

                    if ((new_x, new_y) not in visit and 
                        0 <= new_x < row_limit and 
                        0 <= new_y < col_limit and 
                        grid[new_x][new_y] == 0):

                        que.append((new_x, new_y))
                        visit.add((new_x, new_y))
            
            dist += 1

        return dist - 1 or -1
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxDistance(grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    assert test1 == 2

    test2 = sol.maxDistance(grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    assert test2 == 4
    