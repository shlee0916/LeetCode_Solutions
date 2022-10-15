'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = sorted(nums1 + nums2)
        length = len(total)
        if length % 2 == 0:
            return (total[length // 2] + total[length // 2 - 1]) / 2
        else:
            return (total[length // 2])


if __name__ == "__main__":
    sol = Solution()

    print(sol.findMedianSortedArrays([1, 3], [2]), 2)
    print(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)