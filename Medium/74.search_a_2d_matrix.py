'''
https://leetcode.com/problems/search-a-2d-matrix/description/
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_ver = len(matrix)
        mat_hor = len(matrix[0])

        left = 0
        right = mat_ver * mat_hor - 1

        while left < right:
            mid = (left + right) // 2
            if matrix[mid // mat_hor][mid % mat_hor] < target:
                left = mid + 1
            else:
                right = mid

        return matrix[left // mat_hor][left % mat_hor] == target


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.searchMatrix(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3)
    print(test1, True)
    assert test1 == True

    test2 = sol.searchMatrix(matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13)
    print(test2, False)
    assert test2 == False
