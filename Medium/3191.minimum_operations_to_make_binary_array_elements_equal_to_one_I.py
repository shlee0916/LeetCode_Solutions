'''
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)

        left = 0
        right = 2
        ans = 0

        while right < length:
            if nums[left] == 0:
                ans += 1
                for idx in range(left, left + 3):
                    nums[idx] = 1 if nums[idx] == 0 else 0

            left += 1
            right += 1

        for num in nums:
            if num == 0:
                ans = -1

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(nums = [0, 1, 1, 1, 0, 0])
    assert test1 == 3

    test2 = sol.minOperations(nums = [0, 1, 1, 1])
    assert test2 == -1
    