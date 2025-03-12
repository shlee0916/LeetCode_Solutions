'''
https://leetcode.com/problems/minimum-path-sum/
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        paths = [[0 for _ in range(col)] for _ in range(row)]
        
        for r_num in range(row):
            for c_num in range(col):
                if r_num == 0 and c_num == 0:
                    paths[r_num][c_num] = grid[r_num][c_num]
                    
                else:
                    if r_num > 0 and c_num > 0:
                        paths[r_num][c_num] = min(paths[r_num - 1][c_num], paths[r_num][c_num - 1]) + grid[r_num][c_num]
                    elif r_num > 0:
                        paths[r_num][c_num] = paths[r_num - 1][c_num] + grid[r_num][c_num]
                    else:
                        paths[r_num][c_num] = paths[r_num][c_num - 1] + grid[r_num][c_num]              
                        
        return paths[row - 1][col - 1]


if __name__ == "__main__":
    sol = Solution()

    print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
    print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]), 12)