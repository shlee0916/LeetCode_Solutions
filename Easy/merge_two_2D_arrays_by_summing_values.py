'''
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/?envType=daily-question&envId=2025-03-02
'''

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = []

        num1_idx = 0
        num2_idx = 0

        while num1_idx < len(nums1) and num2_idx < len(nums2):
            if nums1[num1_idx][0] == nums2[num2_idx][0]:
                ans.append([nums1[num1_idx][0], nums1[num1_idx][1] + nums2[num2_idx][1]])
                num1_idx += 1
                num2_idx += 1
            elif nums1[num1_idx][0] > nums2[num2_idx][0]:
                ans.append(nums2[num2_idx])
                num2_idx += 1
            else:
                ans.append(nums1[num1_idx])
                num1_idx += 1
        
        while num1_idx < len(nums1):
            ans.append(nums1[num1_idx])
            num1_idx += 1

        while num2_idx < len(nums2):
            ans.append(nums2[num2_idx])
            num2_idx += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.mergeArrays(nums1 = [[1, 2], [2, 3], [4, 5]], nums2 = [[1, 4], [3, 2], [4, 1]])
    assert test1 == [[1, 6], [2, 3], [3, 2], [4, 6]]

    test2 = sol.mergeArrays(nums1 = [[2, 4], [3, 6], [5, 5]], nums2 = [[1, 3], [4, 3]])
    assert test2 == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
    