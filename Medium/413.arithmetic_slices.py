'''
https://leetcode.com/problems/arithmetic-slices/description/
'''

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        dp, prev_dp = 0, 0
        length = len(nums)

        for idx in range(2, length):
            if nums[idx - 1] - nums[idx - 2] == nums[idx] - nums[idx - 1]:
                dp = prev_dp + 1

            res += dp
            prev_dp = dp
            dp = 0

        return res
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numberOfArithmeticSlices([1, 2, 3, 4])
    print(test1, 3)
    assert test1 == 3
    
    test2 = sol.numberOfArithmeticSlices([1])
    print(test2, 0)
    assert test2 == 0
    