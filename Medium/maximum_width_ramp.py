'''
https://leetcode.com/problems/maximum-width-ramp/?envType=daily-question&envId=2024-10-10
'''

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for idx, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(idx)

        for idx in range(len(nums))[::-1]:
            while stack and nums[stack[-1]] <= nums[idx]:
                ans = max(ans, idx - stack.pop())

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxWidthRamp(nums = [6, 0, 8, 2, 1, 5])
    assert test1 == 4

    test2 = sol.maxWidthRamp(nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
    assert test2 == 7
    