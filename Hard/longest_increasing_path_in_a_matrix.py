'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_limit = len(matrix)
        col_limit = len(matrix[0])

        max_paths = [[-1] * col_limit for _ in range(row_limit)]
        def dfs(row, col, prev):
            if row < 0 or row >= row_limit or col < 0 or col >= col_limit or matrix[row][col] <= prev:
                return 0

            if max_paths[row][col] == -1:
                up = dfs(row + 1, col, matrix[row][col])
                down = dfs(row - 1, col, matrix[row][col])
                left = dfs(row, col - 1, matrix[row][col])
                right = dfs(row, col + 1, matrix[row][col])

                max_paths[row][col] = max(up, down, left, right) + 1

            return max_paths[row][col]

        ans = -1
        for row in range(row_limit):
            for col in range(col_limit):
                ans = max(ans, dfs(row, col, -1))

        return ans

            
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.longestIncreasingPath(matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]])
    assert test1 == 4
    
    test2 = sol.longestIncreasingPath(matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]])
    assert test2 == 4
    
    test3 = sol.longestIncreasingPath(matrix = [[1]])
    assert test3 == 1
    