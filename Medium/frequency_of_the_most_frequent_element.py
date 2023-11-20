'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/?envType=daily-question&envId=2023-11-20
'''

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        for right in range(len(nums)):
            k += nums[right]

            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1

        return right - left + 1


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maxFrequency(nums = [1, 2, 4], k = 5)
    assert test1 == 3

    test2 = sol.maxFrequency(nums = [1, 4, 8, 13], k = 5)
    assert test2 == 2

    test3 = sol.maxFrequency(nums = [3, 9, 6], k = 2)
    assert test3 == 1
    