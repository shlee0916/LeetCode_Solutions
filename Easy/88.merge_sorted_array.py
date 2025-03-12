'''
https://leetcode.com/problems/merge-sorted-array/
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()
        
        
if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    
    sol.merge(nums1, 3, nums2, 3)
    print(nums1)