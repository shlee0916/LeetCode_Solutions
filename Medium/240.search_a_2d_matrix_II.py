'''
https://leetcode.com/problems/search-a-2d-matrix-ii/description/
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1

        return False


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.searchMatrix(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 5)
    print(test1, True)
    assert test1 == True

    test2 = sol.searchMatrix(matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], target = 20)
    print(test2, False)
    assert test2 == False
