'''
https://leetcode.com/problems/uncrossed-lines/description/
'''

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        cross_lines = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for idx_nums1, num1 in enumerate(nums1):
            for idx_nums2, num2 in enumerate(nums2):
                if num1 == num2:
                    cross_lines[idx_nums1 + 1][idx_nums2 + 1] = 1 + cross_lines[idx_nums1][idx_nums2]
                else:
                    cross_lines[idx_nums1 + 1][idx_nums2 + 1] = max(cross_lines[idx_nums1][idx_nums2 + 1], cross_lines[idx_nums1 + 1][idx_nums2])

        return cross_lines[-1][-1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxUncrossedLines(nums1 = [1, 4, 2], nums2 = [1, 2, 4])
    assert test1 == 2

    test2 = sol.maxUncrossedLines(nums1 = [2, 5, 1, 2, 5], nums2 = [10, 5, 2, 1, 5, 2])
    assert test2 == 3

    test3 = sol.maxUncrossedLines(nums1 = [1, 3, 7, 1, 7, 5], nums2 = [1, 9, 2, 5, 1])
    assert test3 == 2
    