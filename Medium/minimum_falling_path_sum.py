'''
https://leetcode.com/problems/minimum-falling-path-sum/description/
'''

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r_idx in range(1, len(matrix)):
            for c_idx, col in enumerate(matrix[0]):
                if c_idx == 0:
                    matrix[r_idx][c_idx] = matrix[r_idx][c_idx] + min(matrix[r_idx - 1][c_idx], matrix[r_idx - 1][c_idx + 1])
                elif c_idx == len(matrix) - 1:
                    matrix[r_idx][c_idx] = matrix[r_idx][c_idx] + min(matrix[r_idx - 1][c_idx - 1], matrix[r_idx - 1][c_idx])
                else:
                    matrix[r_idx][c_idx] = matrix[r_idx][c_idx] + min(matrix[r_idx - 1][c_idx - 1], matrix[r_idx - 1][c_idx], matrix[r_idx - 1][c_idx + 1])


        return min(matrix[-1])


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    print(test1, 13)
    assert test1 == 13

    test2 = sol.minFallingPathSum([[-19, 57], [-40, -5]])
    print(test2, -59)
    assert test2 == -59
