'''
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/
'''

from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        idx_num1 = 0
        idx_num2 = 0
        while idx_num1 < len(nums1) and idx_num2 < len(nums2):
            if nums1[idx_num1] > nums2[idx_num2]:
                idx_num1 += 1
            else:
                ans = max(ans, idx_num2 - idx_num1)
                idx_num2 += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxDistance(nums1 = [55, 30, 5, 4, 2], nums2 = [100, 20, 10, 10, 5])
    assert test1 == 2

    test2 = sol.maxDistance(nums1 = [2, 2, 2], nums2 = [10, 10, 1])
    assert test2 == 1

    test3 = sol.maxDistance(nums1 = [30, 29, 19, 5], nums2 = [25, 25, 25, 25, 25])
    assert test3 == 2
    