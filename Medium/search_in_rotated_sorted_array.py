'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if target < nums[0] < nums[mid]:
                left = mid + 1
            elif target >= nums[0] > nums[mid]:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid

        return -1


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.search(nums = [4, 5, 6, 7, 0, 1, 2], target = 0)
    print(test1, 4)
    assert test1 == 4
    
    test2 = sol.search(nums = [4, 5, 6, 7, 0, 1, 2], target = 3)
    print(test2, -1)
    assert test2 == -1
    
    test3 = sol.search(nums = [1], target = 0)
    print(test3, -1)
    assert test3 == -1
    