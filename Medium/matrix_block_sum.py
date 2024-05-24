'''
https://leetcode.com/problems/matrix-block-sum/description/
'''

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row_range = len(mat)
        col_range = len(mat[0])

        tmp_summation = [[0] * col_range for _ in range(row_range)]

        for row_idx in range(row_range):
            summation = 0
            for col_idx in range(col_range):
                summation += mat[row_idx][col_idx]
                tmp_summation[row_idx][col_idx] = summation

                if row_idx > 0:
                    tmp_summation[row_idx][col_idx] += tmp_summation[row_idx - 1][col_idx]

        ans = [[0] * col_range for _ in range(row_range)]
        for row_idx in range(row_range):
            for col_idx in range(col_range):
                
                min_row = max(0, row_idx - k)
                max_row = min(row_range - 1, row_idx + k)
                min_col = max(0, col_idx - k)
                max_col = min(col_range - 1, col_idx + k)

                ans[row_idx][col_idx] = tmp_summation[max_row][max_col]

                if min_row > 0:
                    ans[row_idx][col_idx] -= tmp_summation[min_row - 1][max_col]

                if min_col > 0:
                    ans[row_idx][col_idx] -= tmp_summation[max_row][min_col - 1]

                if min_row > 0 and min_col > 0:
                    ans[row_idx][col_idx] += tmp_summation[min_row - 1][min_col - 1]

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.matrixBlockSum(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 1)
    assert test1 == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

    test2 = sol.matrixBlockSum(mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 2)
    assert test2 == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
    