'''
https://leetcode.com/problems/maximal-square/
'''
from typing import List


class Solution:
    def maximalSquare(self,  matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        dp_grid = [[0 for _ in row] for row in matrix]
        
        max_size = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == "1":
                    dp_grid[row][col] = (min(dp_grid[row - 1][col - 1], dp_grid[row - 1][col], dp_grid[row][col -1])
                                         + int(matrix[row][col]))

                    max_size = max(max_size, dp_grid[row][col])
                
        return max_size ** 2


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.maximalSquare([["1", "0", "1", "0", "0"],
                             ["1", "0", "1", "1", "1"],
                             ["1", "1", "1", "1", "1"],
                             ["1", "0", "0", "1", "0"]]), 4)
    
    print(sol.maximalSquare([["0", "1"],
                             ["1", "0"]]), 1)
    
    print(sol.maximalSquare([["1", "0", "1", "1", "0", "1"], 
                             ["1", "1", "1", "1", "1", "1"], 
                             ["0", "1", "1", "0", "1", "1"], 
                             ["1", "1", "1", "0", "1", "0"], 
                             ["0", "1", "1", "1", "1", "1"], 
                             ["1", "1", "0", "1", "1", "1"]]), 4)