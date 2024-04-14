'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
'''

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        row_limit = len(heights)
        col_limit = len(heights[0])

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            for delta_row, delta_col in directions:
                new_row = row + delta_row
                new_col = col + delta_col

                if 0 <= new_row < row_limit and 0 <= new_col < col_limit:
                    if heights[new_row][new_col] >= heights[row][col]:
                        dfs(new_row, new_col, visited)

        pacific_set = set()
        atlantic_set = set()
        for row in range(row_limit):
            dfs(row, 0, pacific_set)
            dfs(row, col_limit - 1, atlantic_set)

        for col in range(col_limit):
            dfs(0, col, pacific_set)
            dfs(row_limit - 1, col, atlantic_set)

        return pacific_set & atlantic_set


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.pacificAtlantic(heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    assert test1 == set([(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)])
    
    test2 = sol.pacificAtlantic(heights = [[1]])
    assert test2 == set([(0, 0)])
    