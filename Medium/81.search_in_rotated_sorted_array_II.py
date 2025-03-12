'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False

        left = 0
        right = len(nums) - 1
        while left <= right:

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True

            elif nums[left] <= nums[mid]:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.search(nums = [2, 5, 6, 0, 0, 1, 2], target = 0)
    assert test1 == True

    test2 = sol.search(nums = [2, 5, 6, 0, 0, 1, 2], target = 3)
    assert test2 == False
