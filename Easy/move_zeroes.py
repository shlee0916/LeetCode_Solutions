'''
https://leetcode.com/problems/move-zeroes/description/
'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1


if __name__ == "__main__":
    sol = Solution()
    
    test1_list = [0, 1, 0, 3, 12]
    sol.moveZeroes(test1_list)
    print(test1_list, [1, 3, 12, 0, 0])
    assert test1_list == [1, 3, 12, 0, 0]
    
    test2_list = [0]
    sol.moveZeroes([0])
    print(test2_list,[0])
    assert test2_list == [0]
    