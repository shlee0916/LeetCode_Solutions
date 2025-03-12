'''
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
'''

from typing import List


class Solution:
    # Maybe better way
    def findDifference1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return [list(nums1_set - nums2_set), list(nums2_set- nums1_set)]
    

    def findDifference2(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]

        for num in nums1:
            if num not in nums2 and num not in result[0]:
                result[0].append(num)

        for num in nums2:
            if num not in nums1 and num not in result[1]:
                result[1].append(num)

        return result


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findDifference1(nums1 = [1, 2, 3], nums2 = [2, 4, 6])
    assert test1 == [[1, 3], [4, 6]] 
    
    test2 = sol.findDifference1(nums1 = [1, 2, 3, 3], nums2 = [1, 1, 2, 2])
    assert test2 == [[3], []]
