'''
https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
'''

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_num = len(mat)
        col_num = len(mat[0])
        transpose = list(zip(*mat))

        ans = 0
        for r_idx in range(row_num):
            for c_idx in range(col_num):
                if mat[r_idx][c_idx] == 1 and sum(mat[r_idx]) == 1 and sum(transpose[c_idx]) == 1:
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.numSpecial(mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]])
    assert test1 == 1

    test2 = sol.numSpecial(mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    assert test2 == 3
    