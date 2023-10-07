'''
https://leetcode.com/problems/sort-the-matrix-diagonally/description/
'''

from collections import defaultdict

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])

        list_value = defaultdict(list)
        for row_idx in range(row_len):
            for col_idx in range(col_len):
                list_value[row_idx - col_idx].append(mat[row_idx][col_idx])

        for key in list_value:
            list_value[key].sort(reverse = True)

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                mat[row_idx][col_idx] = list_value[row_idx - col_idx].pop()

        return mat


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.diagonalSort(mat = [[3, 3, 1, 1], 
                                    [2, 2, 1, 2], 
                                    [1, 1, 1, 2]])
    assert test1 == [[1, 1, 1, 1], 
                     [1, 2, 2, 2], 
                     [1, 2, 3, 3]]

    test2 = sol.diagonalSort(mat = [[11, 25, 66, 1, 69, 7], 
                                    [23, 55, 17, 45, 15, 52], 
                                    [75, 31, 36, 44, 58, 8], 
                                    [22, 27, 33, 25, 68, 4], 
                                    [84, 28, 14, 11, 5, 50]])
    assert test2 == [[5, 17, 4, 1, 52, 7], 
                     [11, 11, 25, 45, 8, 69], 
                     [14, 23, 25, 44, 58, 15], 
                     [22, 27, 31, 36, 50, 66], 
                     [84, 28, 75, 33, 55, 68]]
    