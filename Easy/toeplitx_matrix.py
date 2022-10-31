'''
https://leetcode.com/problems/toeplitz-matrix/
'''
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for idx, row in enumerate(matrix[:-1]):
            if row[:-1] != matrix[idx + 1][1:]:
                return False
            
        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]), True)
    print(sol.isToeplitzMatrix([[1, 2], [2, 2]]), False)