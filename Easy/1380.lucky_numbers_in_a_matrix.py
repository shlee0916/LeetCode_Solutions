'''
https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
'''

from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [min(row) for row in matrix]
        max_col = [max(col) for col in zip(*matrix)]

        ans = []
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if min_row[row_idx] == max_col[col_idx]:
                    ans.append(val)

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.luckyNumbers(matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]])
    assert test1 == [15]
    
    test2 = sol.luckyNumbers(matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]])
    assert test2 == [12]
    
    test3 = sol.luckyNumbers(matrix = [[7, 8], [1, 2]])
    assert test3 == [7]
    