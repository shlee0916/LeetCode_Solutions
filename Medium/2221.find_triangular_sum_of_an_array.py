'''
https://leetcode.com/problems/find-triangular-sum-of-an-array/description/
'''

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for idx in range(len(nums) - 1):
                nums[idx] += nums[idx + 1]
                nums[idx] %= 10

            nums.pop()

        return nums[0]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.triangularSum(nums = [1, 2, 3, 4, 5])
    assert test1 == 8

    test2 = sol.triangularSum(nums = [5])
    assert test2 == 5
    