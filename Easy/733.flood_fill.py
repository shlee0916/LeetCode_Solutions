'''
https://leetcode.com/problems/flood-fill/description/
'''

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_limit = len(image)
        col_limit = len(image[0])
        origin_color = image[sr][sc]

        def dfs(row, col):
            if (not (0 <= row < row_limit and 0 <= col < col_limit)) or image[row][col] != origin_color:
                return

            image[row][col] = color

            for delta_row, delta_col in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(row + delta_row, col + delta_col)

        if origin_color != color:
            dfs(sr, sc)

        return image
            
            
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.floodFill(image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2)
    assert test1 == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    test2 = sol.floodFill(image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0)
    assert test2 == [[0, 0, 0], [0, 0, 0]]
