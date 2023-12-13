'''
https://leetcode.com/problems/map-of-highest-peak/description/
'''

from collections import deque

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row_len = len(isWater)
        col_len = len(isWater[0])

        water_cells = []
        for r_idx in range(row_len):
            for c_idx in range(col_len):
                if isWater[r_idx][c_idx] == 1:
                    water_cells.append((r_idx, c_idx))

        new_land = [[-1] * col_len for _ in range(row_len)]
        for water_row, water_col in water_cells:
            new_land[water_row][water_col] = 0

        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        que = deque(water_cells)
        while que:
            cur_row, cur_col = que.popleft()

            for delta_row, delta_col in delta:
                new_row, new_col = cur_row + delta_row, cur_col + delta_col
                if 0 <= new_row < row_len and 0 <= new_col < col_len and new_land[new_row][new_col] == -1:
                    new_land[new_row][new_col] = new_land[cur_row][cur_col] + 1
                    que.append((new_row, new_col))
    
        return new_land


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.highestPeak(isWater = [[0, 1], [0, 0]])
    assert test1 == [[1, 0], [2, 1]]

    test2 = sol.highestPeak(isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]])
    assert test2 == [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
    