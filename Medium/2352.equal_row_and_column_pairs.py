'''
https://leetcode.com/problems/equal-row-and-column-pairs/description/
'''

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        degree90 = [list(col) for col in zip(*grid)]
        for row in grid:
            cnt += degree90.count(row)

        return cnt
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.equalPairs(grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]])
    assert test1 == 1
    
    test2 = sol.equalPairs(grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
    assert test2 == 3
    