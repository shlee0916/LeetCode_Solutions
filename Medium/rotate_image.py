'''
https://leetcode.com/problems/rotate-image/
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(row) for row in zip(*matrix[::-1])]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 1]]
    sol.rotate(matrix)
    print(matrix)