'''
https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09
'''

from typing import List


class Solution:
    def is_magic_square(self, square: List[List[int]]) -> bool:
        nums = [num for row in square for num in row]
        if sorted(nums) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

        sums = []
        row_sums = [sum(row) for row in square]
        col_sums = [sum(col) for col in list(zip(*square))]
        diag_sums = [sum(square[idx][idx] for idx in range(3)), square[0][2] + square[1][1] + square[2][0]]

        sums.extend(row_sums)
        sums.extend(col_sums)
        sums.extend(diag_sums)

        return len(set(sums)) == 1


    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        if len(grid) < 3 or len(grid[0]) < 3:
            return ans

        for row_idx in range(len(grid) - 2):
            for col_idx in range(len(grid[0]) - 2):
                square = [grid[row_idx + idx][col_idx : col_idx + 3] for idx in range(3)]

                if self.is_magic_square(square):
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numMagicSquaresInside(grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])
    assert test1 == 1

    test2 = sol.numMagicSquaresInside(grid = [[8]])
    assert test2 == 0
