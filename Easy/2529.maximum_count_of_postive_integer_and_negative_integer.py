'''
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/?envType=daily-question&envId=2025-03-12
'''

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bs(target):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1

            return right + 1

        neg_nums = bs(0)
        pos_nums = len(nums) - bs(1)

        return max(neg_nums, pos_nums)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumCount(nums = [-2, -1, -1, 1, 2, 3])
    assert test1 == 3

    test2 = sol.maximumCount(nums = [-3, -2, -1, 0, 0, 1, 2])
    assert test2 == 3

    test3 = sol.maximumCount(nums = [5, 20, 66, 1314])
    assert test3 == 4
