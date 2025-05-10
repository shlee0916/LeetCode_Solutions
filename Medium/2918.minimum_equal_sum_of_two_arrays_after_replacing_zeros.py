'''
https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/?envType=daily-question&envId=2025-05-10
'''

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_zero = nums1.count(0)
        nums2_zero = nums2.count(0)

        nums1_total = sum(nums1)
        nums2_total = sum(nums2)

        min_num1 = nums1_total + nums1_zero
        min_num2 = nums2_total + nums2_zero

        if (min_num1 > min_num2 and nums2_zero == 0) or (min_num2 > min_num1 and nums1_zero == 0):
            return -1

        return max(nums1_zero + nums1_total, nums2_zero + nums2_total)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minSum(nums1 = [3, 2, 0, 1, 0], nums2 = [6, 5, 0])
    assert test1 == 12
    
    test2 = sol.minSum(nums1 = [2, 0, 2, 0], nums2 = [1, 4])
    assert test2 == -1
    