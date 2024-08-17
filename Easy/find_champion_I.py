'''
https://leetcode.com/problems/find-champion-i/description/
'''

from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for idx, team in enumerate(grid):
            if sum(team) == len(grid) - 1:
                return idx


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findChampion(grid = [[0, 1], [0, 0]])
    assert test1 == 0
    
    test2 = sol.findChampion(grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]])
    assert test2 == 1
    