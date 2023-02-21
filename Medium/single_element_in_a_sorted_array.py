'''
https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print(test1, 2)
    assert test1 == 2

    test2 = sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
    print(test2, 10)
    assert test2 == 10
    