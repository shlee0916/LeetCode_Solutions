'''
https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01
'''

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(len(nums)):
            if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                nums[right] *= 2
                nums[right + 1] = 0
            
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.applyOperations(nums = [1, 2, 2, 1, 1, 0])
    assert test1 == [1, 4, 2, 0, 0, 0]
    
    test2 = sol.applyOperations(nums = [0, 1])
    assert test2 == [1, 0]
    