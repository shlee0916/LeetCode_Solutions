'''
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2024-11-13
'''

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def cnt(target):
            res = 0
            left = 0
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res += right - left 
                    left += 1
            return res

        nums.sort()
        
        return cnt(upper) - cnt(lower - 1)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.countFairPairs(nums = [0, 1, 7, 4, 4, 5], lower = 3, upper = 6)
    assert test1 == 6

    test2 = sol.countFairPairs(nums = [1, 7, 9, 2, 5], lower = 11, upper = 11)
    assert test2 == 1
