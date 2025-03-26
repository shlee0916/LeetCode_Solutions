'''
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/?envType=daily-question&envId=2025-03-26
'''

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        grid_vals = []
        for row in grid:
            grid_vals.extend(row)

        grid_vals.sort()
        
        mid_val = grid_vals[len(grid_vals) // 2]
        cnt = 0
        for num in grid_vals:
            diff = abs(num - mid_val)
            if diff % x != 0:
                return -1

            cnt += diff // x

        return cnt
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(grid = [[2, 4], [6, 8]], x = 2)
    assert test1 == 4

    test2 = sol.minOperations(grid = [[1, 5], [2, 3]], x = 1)
    assert test2 == 5

    test3 = sol.minOperations(grid = [[1, 2], [3, 4]], x = 2)
    assert test3 == -1
    