'''
https://leetcode.com/problems/product-of-array-except-self/description/
'''

from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = reduce(lambda a, b: a * (b if b else 1), nums, 1), nums.count(0)

        if zero_cnt > 1:
            return [0] * len(nums)

        for idx, num in enumerate(nums):
            if zero_cnt:
                nums[idx] = 0 if num else prod
            else:
                nums[idx] = prod // num

        return nums


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.productExceptSelf(nums = [1, 2, 3, 4])
    print(test1, [24, 12, 8, 6])
    assert test1 == [24, 12, 8, 6]
    
    test2 = sol.productExceptSelf(nums = [-1, 1, 0, -3, 3])
    print(test2, [0, 0, 9, 0, 0])
    assert test2 == [0, 0, 9, 0, 0]
    