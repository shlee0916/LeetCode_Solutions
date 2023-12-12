'''
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2023-12-12
'''

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxProduct(nums = [3, 4, 5, 2])
    assert test1 == 12

    test2 = sol.maxProduct(nums = [1, 5, 4, 5])
    assert test2 == 16

    test3 = sol.maxProduct(nums = [3, 7])
    assert test3 == 12
    