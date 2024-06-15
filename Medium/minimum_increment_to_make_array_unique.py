'''
https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14
'''

from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                ans += nums[idx - 1] - nums[idx] + 1
                nums[idx] = nums[idx - 1] + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.minIncrementForUnique(nums = [1, 2, 2])
    assert test1 == 1
    
    test2 = sol.minIncrementForUnique(nums = [3, 2, 1, 2, 1, 7])
    assert test2 == 6
    