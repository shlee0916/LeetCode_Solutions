'''
https://leetcode.com/problems/set-matrix-zeroes/
'''
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        
        for r_idx, r in enumerate(matrix):
            for c_idx, c in enumerate(r):
                if c == 0:
                    rows.add(r_idx)
                    cols.add(c_idx)
                    
        for r_idx in rows:
            matrix[r_idx] = [0] * len(matrix[0])
            
        for r_idx, row in enumerate(matrix):
            for c_idx, _ in enumerate(row):
                if c_idx in cols:
                    matrix[r_idx][c_idx] = 0
                
                
if __name__ == "__main__":
    sol = Solution()
    
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    
    sol.setZeroes(matrix1)
    print(matrix1, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])
    assert matrix1, [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    
    sol.setZeroes(matrix2)
    print(matrix2, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
    assert matrix2, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]