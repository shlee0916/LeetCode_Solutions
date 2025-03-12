'''
https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
'''

from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        ans = 0
        for vals in zip(*grid):
            ans += max(vals)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.deleteGreatestValue(grid = [[1, 2, 4], [3, 3, 1]])
    assert test1 == 8
    
    test2 = sol.deleteGreatestValue(grid = [[10]])
    assert test2 == 10
    