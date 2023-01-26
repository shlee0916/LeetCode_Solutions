'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findMin(nums = [3, 4, 5, 1, 2])
    print(test1, 1)
    assert test1 == 1

    test2 = sol.findMin(nums = [4, 5, 6, 7, 0, 1, 2])
    print(test2, 0)
    assert test2 == 0

    test3 = sol.findMin(nums = [11, 13, 15, 17])
    print(test3, 11)
    assert test3 == 11
    