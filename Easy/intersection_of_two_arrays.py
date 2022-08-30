'''
https://leetcode.com/problems/intersection-of-two-arrays/
'''
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checked = []
        ans = []
        if len(nums1) > len(nums2):
            for num in nums2:
                if num not in checked and num in nums1:
                    ans.append(num)
                    checked.append(num)
        else:
            for num in nums1:
                if num not in checked and num in nums2:
                    ans.append(num)
                    checked.append(num)
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.intersection([1, 2, 3], [2 ,3, 3, 4]))