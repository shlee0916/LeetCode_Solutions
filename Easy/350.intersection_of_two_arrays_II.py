'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
'''

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        ans = []
        idx_1 = 0
        idx_2 = 0

        while idx_1 < len(nums1) and idx_2 < len(nums2):
            if nums1[idx_1] < nums2[idx_2]:
                idx_1 += 1
            elif nums2[idx_2] < nums1[idx_1]:
                idx_2 += 1
            else:
                ans.append(nums1[idx_1])
                idx_1 += 1
                idx_2 += 1

        return ans
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.intersect(nums1 = [1, 2, 2, 1], nums2 = [2, 2])
    assert test1 == [2, 2]
    
    test2 = sol.intersect(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4])
    assert test2 == [4, 9]
    