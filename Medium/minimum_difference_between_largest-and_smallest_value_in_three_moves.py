'''
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03
'''

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0

        nums.sort()

        ans = min(nums[-1] - nums[3], 
                nums[-2] - nums[2],
                nums[-3] - nums[1],
                nums[-4] - nums[0])

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minDifference(nums = [5, 3, 2, 4])
    assert test1 == 0

    test2 = sol.minDifference(nums = [1, 5, 0, 10, 14])
    assert test2 == 1

    test3 = sol.minDifference(nums = [3, 100, 20])
    assert test3 == 0
    