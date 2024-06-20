'''
https://leetcode.com/problems/minimum-common-value/
'''

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1_pointer = 0
        n2_pointer = 0

        while n1_pointer < len(nums1) and n2_pointer < len(nums2):
            if nums1[n1_pointer] == nums2[n2_pointer]:
                return nums1[n1_pointer]
            
            elif nums1[n1_pointer] > nums2[n2_pointer]:
                n2_pointer += 1
            else:
                n1_pointer += 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getCommon(nums1 = [1, 2, 3], nums2 = [2, 4])
    assert test1 == 2

    test2 = sol.getCommon(nums1 = [1, 2, 3, 6], nums2 = [2, 3, 4, 5])
    assert test2 == 2
