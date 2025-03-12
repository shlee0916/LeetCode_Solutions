'''
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
'''

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        return nums[-1] * nums[-2] - nums[0] * nums[1]


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maxProductDifference(nums = [5, 6, 2, 7, 4])
    assert test1 == 34
    
    test2 = sol.maxProductDifference(nums = [4, 2, 5, 9, 7, 4, 8])
    assert test2 == 64
    