'''
https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] >= nums[right] else right


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findPeakElement(nums = [1, 2, 3, 1])
    assert test1 == 2

    test2 = sol.findPeakElement(nums = [1, 2, 1, 3, 5, 6, 4])
    assert test2 == 5
