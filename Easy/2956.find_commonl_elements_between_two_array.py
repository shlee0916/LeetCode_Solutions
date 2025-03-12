'''
https://leetcode.com/problems/find-common-elements-between-two-arrays/
'''

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        nums1_cnt = sum(1 for num in nums1 if num in nums2_set)
        nums2_cnt = sum(1 for num in nums2 if num in nums1_set)

        return [nums1_cnt, nums2_cnt]
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findIntersectionValues(nums1 = [4, 3, 2, 3, 1], nums2 = [2, 2, 5, 2, 3, 6])
    assert test1 == [3, 4]
    
    test2 = sol.findIntersectionValues(nums1 = [3, 4, 2, 3], nums2 = [1, 5])
    assert test2 == [0, 0]
    