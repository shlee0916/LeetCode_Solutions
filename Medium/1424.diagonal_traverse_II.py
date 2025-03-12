'''
https://leetcode.com/problems/diagonal-traverse-ii/description/?envType=daily-question&envId=2023-11-22
'''

from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        values = []
        for r_idx, row in enumerate(nums):
            for c_idx, num in enumerate(row):
                values.append((r_idx + c_idx, r_idx, num))

        values.sort(key = lambda x: (x[0], -x[1]))

        return [num for _, _, num in values]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findDiagonalOrder(nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert test1 == [1, 4, 2, 7, 5, 3, 8, 6, 9]

    test2 = sol.findDiagonalOrder(nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]])
    assert test2 == [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
    