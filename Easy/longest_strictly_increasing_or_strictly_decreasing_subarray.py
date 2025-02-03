'''
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2025-02-03
'''

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = 1
        max_dec = 1
        cur_inc = 1
        cur_dec = 1

        for idx in range(1, len(nums)):
            if nums[idx - 1] < nums[idx]:
                cur_inc += 1
            else:
                cur_inc = 1

            if nums[idx - 1] > nums[idx]:
                cur_dec += 1
            else:
                cur_dec = 1
            
            max_inc = max(max_inc, cur_inc)
            max_dec = max(max_dec, cur_dec)

        return max(max_inc, max_dec)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestMonotonicSubarray(nums = [1, 4, 3, 3, 2])
    assert test1 == 2

    test2 = sol.longestMonotonicSubarray(nums = [3, 3, 3, 3])
    assert test2 == 1

    test3 = sol.longestMonotonicSubarray(nums = [3, 2, 1])
    assert test3 == 3
