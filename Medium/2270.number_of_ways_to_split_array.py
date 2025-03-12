'''
https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03
'''

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)

        ans = 0
        cur_sum = 0
        for idx in range(len(nums) - 1):
            cur_sum += nums[idx]

            if cur_sum >= total - cur_sum:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.waysToSplitArray(nums = [10, 4, -8, 7])
    assert test1 == 2
    
    test2 = sol.waysToSplitArray(nums = [2, 3, 1, 0])
    assert test2 == 2
    