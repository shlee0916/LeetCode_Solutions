'''
https://leetcode.com/problems/matrix-diagonal-sum/description/
'''

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)

        result = 0
        for row_idx in range(row // 2):
            result += mat[row_idx][row_idx] + mat[row_idx][-row_idx - 1]
            result += mat[-row_idx - 1][row_idx] + mat[-row_idx - 1][-row_idx - 1]

        if row % 2 == 1:
            result += mat[row // 2][row // 2]

        return result


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.diagonalSum(mat = [[1, 2, 3], 
                                    [4, 5, 6], 
                                    [7, 8, 9]])
    assert test1 == 25
    
    test2 = sol.diagonalSum(mat = [[1, 1, 1, 1], 
                                    [1, 1, 1, 1], 
                                    [1, 1, 1, 1], 
                                    [1, 1, 1, 1]])
    assert test2 == 8
    
    test3 = sol.diagonalSum(mat = [[5]])
    assert test3 == 5
    