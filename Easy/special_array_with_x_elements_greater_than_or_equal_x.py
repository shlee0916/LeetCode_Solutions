'''
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/?envType=daily-question&envId=2024-05-27
'''

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return -1 if left < len(nums) and left == nums[left] else left


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.specialArray(nums = [3, 5])
    assert test1 == 2

    test2 = sol.specialArray(nums = [0, 0])
    assert test2 == -1

    test3 = sol.specialArray(nums = [0, 4, 3, 0, 4])
    assert test3 == 3
    