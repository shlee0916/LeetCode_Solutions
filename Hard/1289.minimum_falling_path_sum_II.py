'''
https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
'''

from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        length = len(grid)
        res = float("inf")

        dp = [[-1] * length for _ in range(length)]
        for idx in range(length):
            dp[0][idx] = grid[0][idx]

        for row_idx in range(1, length):
            for col_idx in range(length):
                cur_val = float("inf")

                for idx in range(length):
                    if idx != col_idx:
                        cur_val = min(cur_val, grid[row_idx][col_idx] + dp[row_idx - 1][idx])

                dp[row_idx][col_idx] = cur_val

        for col_idx in range(length):
            res = min(res, dp[length - 1][col_idx])
        
        return res
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minFallingPathSum(grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert test1 == 13
    
    test2 = sol.minFallingPathSum(grid = [[7]])
    assert test2 == 7
    