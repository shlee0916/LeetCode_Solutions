'''
https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/?envType=daily-question&envId=2025-06-12
'''

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = abs(nums[0] - nums[-1])

        for idx in range(len(nums) - 1):
            ans = max(ans, abs(nums[idx + 1] - nums[idx]))

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxAdjacentDistance(nums = [1, 2, 4])
    assert test1 == 3

    test2 = sol.maxAdjacentDistance(nums = [-5, -10, -5])
    assert test2 == 5
