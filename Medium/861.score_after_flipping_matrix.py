'''
https://leetcode.com/problems/score-after-flipping-matrix/?envType=daily-question&envId=2024-05-13
'''

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for idx in range(len(row)):
                    row[idx] = 1 if row[idx] == 0 else 0

        col2row = [list(row) for row in zip(*grid)]
        new_grid = [[str(num) for num in col2row[0]]]
        for col in col2row[1:]:
            new_row = []
            if col.count(0) > col.count(1):
                new_grid.append(["1" if num == 0 else "0" for num in col])
            else:
                new_grid.append([str(num) for num in col])

        ans = 0
        for row in list(zip(*new_grid)):
            ans += int("".join(row), 2)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.matrixScore(grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    assert test1 == 39
    
    test2 = sol.matrixScore(grid = [[0]])
    assert test2 == 1
    