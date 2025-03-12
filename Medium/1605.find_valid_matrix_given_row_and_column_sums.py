'''
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/
'''

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row_num = len(rowSum)
        col_num = len(colSum)

        matrix = [[0 for _ in range(col_num)] for _ in range(row_num)]

        for r_idx in range(row_num):
            for c_idx in range(col_num):
                r_sum = rowSum[r_idx]
                c_sum = colSum[c_idx]
                min_val = min(r_sum, c_sum)
                
                matrix[r_idx][c_idx] = min_val

                rowSum[r_idx] -= min_val
                colSum[c_idx] -= min_val

        return matrix


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.restoreMatrix(rowSum = [3, 8], colSum = [4, 7])
    assert test1 == [[3, 0],
                     [1, 7]]
    
    test2 = sol.restoreMatrix(rowSum = [5, 7, 10], colSum = [8, 6, 8])
    assert test2 == [[5, 0, 0], 
                     [3, 4, 0], 
                     [0, 2, 8]]
    