'''
https://leetcode.com/problems/shortest-bridge/description/
'''

from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            grid[row][col] = -1
            que.append((row, col))

            for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = row + delta_row, col + delta_col

                if 0 <= new_row < row_len and 0 <= new_col < col_len:
                    if grid[new_row][new_col] == 1:
                        dfs(new_row, new_col)

        def get_island():
            for row_idx in range(row_len):
                for col_idx in range(col_len):
                    if grid[row_idx][col_idx] == 1:
                        return row_idx, col_idx

        row_len = len(grid)
        col_len = len(grid[0])
        que = []
        
        start_row, start_col = get_island()
        dfs(start_row, start_col)

        path_len = 0
        while que:
            new_points = []

            for row, col in que:
                for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_row, new_col = row + delta_row, col + delta_col

                    if 0 <= new_row < row_len and 0 <= new_col < col_len:
                        if grid[new_row][new_col] == 1:
                            return path_len
                        elif grid[new_row][new_col] == 0:
                            grid[new_row][new_col] = -1
                            new_points.append((new_row, new_col))

            path_len += 1
            que = new_points

        return -1
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.shortestBridge(grid = [[0, 1], [1, 0]])
    assert test1 == 1
    
    test2 = sol.shortestBridge(grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]])
    assert test2 == 2
    
    test3 = sol.shortestBridge(grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
    assert test3 == 1
    