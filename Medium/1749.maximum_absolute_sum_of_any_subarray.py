'''
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
'''

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = pos_max = neg_min = 0

        for num in nums:
            pos_max = max(pos_max + num, 0)
            neg_min = min(neg_min + num, 0)
            ans = max(ans, pos_max, -neg_min)

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxAbsoluteSum(nums = [1, -3, 2, 3, -4])
    assert test1 == 5

    test2 = sol.maxAbsoluteSum(nums = [2, -5, 1, -4, 3, -2])
    assert test2 == 8
    