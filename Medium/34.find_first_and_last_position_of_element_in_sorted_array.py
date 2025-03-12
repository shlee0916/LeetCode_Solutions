'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsearch(arr, target_num):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target_num:
                    right = mid
                else:
                    left = mid + 1

            return left

        left = bsearch(nums, target)
        right = bsearch(nums, target + 1) - 1

        return [left, right] if target in nums[left:left + 1] else [-1, -1]
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.searchRange(nums = [5, 7, 7, 8, 8, 10], target = 8)
    print(test1, [3, 4])
    assert test1 == [3, 4]
    
    test2 = sol.searchRange(nums = [5, 7, 7, 8, 8, 10], target = 6)
    print(test2, [-1, -1])
    assert test2 == [-1, -1]
    
    test3 = sol.searchRange(nums = [], target = 0)
    print(test3, [-1, -1])
    assert test3 == [-1, -1]
    