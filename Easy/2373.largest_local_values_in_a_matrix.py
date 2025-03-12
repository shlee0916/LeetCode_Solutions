'''
https://leetcode.com/problems/largest-local-values-in-a-matrix/?envType=daily-question&envId=2024-05-12
'''

from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)

        ans = []
        for r_idx in range(1, length - 1):
            temp_row = []
            for c_idx in range(1, length - 1):
                temp_row.append(
                    max(grid[row][col] for row in range(r_idx - 1, r_idx + 2) for col in range(c_idx - 1, c_idx + 2))
                )

            ans.append(temp_row)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.largestLocal(grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
    assert test1 == [[9, 9], [8, 6]]
    
    test2 = sol.largestLocal(grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    assert test2 == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    