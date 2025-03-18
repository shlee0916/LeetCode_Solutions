'''
https://leetcode.com/problems/longest-nice-subarray/description/?envType=daily-question&envId=2025-03-18
'''

from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        and_bit = 0
        left = 0
        for right in range(len(nums)):
            while and_bit & nums[right]:
                and_bit ^= nums[left]
                left += 1

            and_bit |= nums[right]
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.longestNiceSubarray(nums = [1, 3, 8, 48, 10])
    assert test1 == 3

    test2 = sol.longestNiceSubarray(nums = [3, 1, 5, 11, 13])
    assert test2 == 1
    