'''
https://leetcode.com/problems/reshape-the-matrix/description/
'''

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flatten = []
        new_mat = []

        for row in mat:
            for value in row:
                flatten.append(value)

        if r * c != len(flatten):
            return mat
        else:
            new_mat.extend(flatten[row_idx * c : row_idx * c + c] for row_idx in range(r))

        return new_mat


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.matrixReshape(mat = [[1, 2], [3, 4]], r = 1, c = 4)
    assert test1 == [[1, 2, 3, 4]]
    
    test2 = sol.matrixReshape(mat = [[1, 2], [3, 4]], r = 2, c = 4)
    assert test2 == [[1, 2], [3, 4]]
    