'''
https://leetcode.com/problems/sort-array-by-parity/description/?envType=daily-question&envId=2023-09-28
'''

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]

        return nums


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.sortArrayByParity(nums = [3,1,2,4])
    assert test1 == [4, 2, 1, 3]
    
    test2 = sol.sortArrayByParity(nums = [0])
    assert test2 == [0]
    