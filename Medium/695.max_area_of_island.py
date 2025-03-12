'''
https://leetcode.com/problems/max-area-of-island/
'''

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pos_stack = []

        ver_len = len(grid)
        hor_len = len(grid[0])
        max_island = 0
        for ver_pos in range(ver_len):
            for hor_pos in range(hor_len):

                if grid[ver_pos][hor_pos]:
                    pos_stack.append((ver_pos, hor_pos))
                    grid[ver_pos][hor_pos] = 0
                    cur_island = 0

                    while pos_stack:
                        ver_pos, hor_pos = pos_stack.pop()
                        cur_island += 1
                        if ver_pos < ver_len - 1 and grid[ver_pos + 1][hor_pos]:
                            pos_stack.append((ver_pos + 1, hor_pos))
                            grid[ver_pos + 1][hor_pos] = 0
                        if ver_pos > 0 and grid[ver_pos - 1][hor_pos]:
                            pos_stack.append((ver_pos - 1, hor_pos))
                            grid[ver_pos - 1][hor_pos] = 0
                        if hor_pos < hor_len - 1 and grid[ver_pos][hor_pos + 1]:
                            pos_stack.append((ver_pos, hor_pos + 1))
                            grid[ver_pos][hor_pos + 1] = 0
                        if hor_pos > 0 and grid[ver_pos][hor_pos - 1]:
                            pos_stack.append((ver_pos, hor_pos - 1))
                            grid[ver_pos][hor_pos - 1] = 0

                    max_island = max(max_island, cur_island)

        return max_island


if __name__ == "__main__":
    sol = Solution()

    test1_grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], 
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
    test1 = sol.maxAreaOfIsland(test1_grid)
    print(test1, 6)
    assert test1 == 6

    test2_grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    test2 = sol.maxAreaOfIsland(test2_grid)
    print(test2, 0)
    assert test2 == 0

    test3_grid = [
        [1, 1, 0, 0, 0], 
        [1, 1, 0, 0, 0], 
        [0, 0, 0, 1, 1], 
        [0, 0, 0, 1, 1]
        ]
    test3 = sol.maxAreaOfIsland(test3_grid)
    print(test3, 4)
    assert test3 == 4
