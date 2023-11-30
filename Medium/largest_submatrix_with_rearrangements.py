'''
https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2023-11-30
'''

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row_limit = len(matrix)
        col_limit = len(matrix[0])

        ans = 0
        heights = [0] * col_limit

        for r_idx in range(row_limit):
            for c_idx in range(col_limit):
                if matrix[r_idx][c_idx] == 0:
                    heights[c_idx] = 0
                else:
                    heights[c_idx] += 1

            sorted_height = sorted(heights)
            for idx, height in enumerate(sorted_height):
                ans =  max(ans, height * (col_limit - idx))

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.largestSubmatrix(matrix = [[0, 0, 1], [1, 1, 1], [1, 0, 1]])
    assert test1 == 4

    test2 = sol.largestSubmatrix(matrix = [[1, 0, 1, 0, 1]])
    assert test2 == 3

    test3 = sol.largestSubmatrix(matrix = [[1, 1, 0], [1, 0, 1]])
    assert test3 == 2
    